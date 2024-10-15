from odoo import models, fields, api
from lxml import etree

class InheritModuleTestShub(models.Model):
    _inherit = 'hr.employee'

    marital_ShubCreated = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('cohabitant', 'Legal Cohabitant'),
        ('widower', 'Widower'),
        ('divorced', 'Divorced')
    ], string='Marital Status', groups="hr.group_hr_user", default='single', tracking=True)

    spouse_complete_name_ShubCreated = fields.Char(string="Spouse Complete Name", groups="hr.group_hr_user", tracking=True)
    spouse_birthdate_ShubCreated = fields.Date(string="Spouse Birthdate", groups="hr.group_hr_user", tracking=True)

    children_ShubCreated = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ], string='Number of Dependent Children', groups="hr.group_hr_user", tracking=True)

    def _create_child_fields(self):
        for i in range(1, 6):
            setattr(self.__class__, f'child_name_{i}', fields.Char(string=f'Child Name {i}'))
            setattr(self.__class__, f'child_gender_{i}', fields.Selection([
                ('male', 'Male'),
                ('female', 'Female'),
                ('other', 'Other')
            ], string=f'Child Gender {i}'))

    locals().update(_create_child_fields(None))






    @api.model
    def _get_child_details_view(self):
        arch = '''
        <group string="Children Details" invisible="children_ShubCreated == '0'">
        '''
        for i in range(1, 6):
            arch += f'''
            <field name="child_name_{i}" invisible="children_ShubCreated in {[str(n) for n in range(i)]}"/>
            <field name="child_gender_{i}" invisible="children_ShubCreated in {[str(n) for n in range(i)]}"/>
            '''
        arch += '</group>'
        return arch

    @api.model
    def fields_view_get(self, view_id="hr.employee", view_type='form', toolbar=False, submenu=False):
        res = super(InheritModuleTestShub, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        if view_type == 'form':
            doc = etree.XML(res['arch'])
            for i in doc.xpath("//group[@string='Family Status Shub Created']"):
                child_details = etree.fromstring(self._get_child_details_view())
                i.append(child_details)
            res['arch'] = etree.tostring(doc, encoding='unicode')
        return res


    @api.model
    def init(self):
        super(InheritModuleTestShub, self).init()