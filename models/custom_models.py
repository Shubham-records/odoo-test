from odoo import models, fields, api

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
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ], string='Number of Dependent Children', groups="hr.group_hr_user", tracking=True)


    def _create_child_fields(self):
        child_fields = {}
        for i in range(1, 6):
            child_fields[f'child_name_{i}'] = fields.Char(string=f'Child Name {i}')
            child_fields[f'child_gender_{i}'] = fields.Selection([
                ('male', 'Male'),
                ('female', 'Female'),
                ('other', 'Other')
            ], string=f'Child Gender {i}')
        return child_fields

    locals().update(_create_child_fields(None))





