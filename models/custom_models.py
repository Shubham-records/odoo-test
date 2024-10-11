from odoo import models, fields, api

class Child(models.Model):
    _name = 'employee.child'
    _description = 'Child Details'

    name = fields.Char(string='Child Name', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', required=True)
    employee_id = fields.Many2one('hr.employee', string='Employee')


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
    children_ShubCreated = fields.Integer(string='Number of Dependent Children', groups="hr.group_hr_user", tracking=True)

    children_ids = fields.One2many('employee.child', 'employee_id', string='Children')

    @api.onchange('children_ShubCreated')
    def _onchange_children_ShubCreated(self):
        if self.children_ShubCreated >= 0:
            existing_lines = len(self.children_ids)
            if self.children_ShubCreated > existing_lines:
                for _ in range(self.children_ShubCreated - existing_lines):
                    self.children_ids.new({'name': '', 'gender': 'male'})







    # names = fields.Text(string='Child Names', default='', required=False)
    # genders = fields.Text(string='Child Genders', default='', required=False)

    # @api.onchange('children_ShubCreated')
    # def _onchange_children_ShubCreated(self):
    #     self.children_ShubCreated = max(self.children_ShubCreated, 0)

    #     names = [name.strip() for name in self.names.split(',')] if self.names else []
    #     genders = [gender.strip() for gender in self.genders.split(',')] if self.genders else []

    #     if self.children_ShubCreated > len(names):
    #         names += [''] * (self.children_ShubCreated - len(names))
    #     elif self.children_ShubCreated < len(names):
    #         names = names[:self.children_ShubCreated]

    #     if self.children_ShubCreated > len(genders):
    #         genders += [''] * (self.children_ShubCreated - len(genders))
    #     elif self.children_ShubCreated < len(genders):
    #         genders = genders[:self.children_ShubCreated]

    #     # Update the fields with adjusted lists
    #     self.names = ', '.join(names)
    #     self.genders = ', '.join(genders)

            
            
