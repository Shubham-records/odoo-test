from odoo import models, fields, api

class inherit_module_test_shub(models.Model):

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



        