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
    ],string='Number of Dependent Children', groups="hr.group_hr_user", tracking=True)


    child_name_1 = fields.Char(string='Child Name 1')
    child_gender_1 = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Child Gender 1')

    child_name_2 = fields.Char(string='Child Name 2')
    child_gender_2 = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Child Gender 2')

    child_name_3 = fields.Char(string='Child Name 3')
    child_gender_3 = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Child Gender 3')

    child_name_4 = fields.Char(string='Child Name 4')
    child_gender_4 = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Child Gender 4')

    child_name_5 = fields.Char(string='Child Name 5')
    child_gender_5 = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Child Gender 5')






    # @api.onchange('children_ShubCreated')
    # def _onchange_children_ShubCreated(self):
    #     self.child_name_1 = False
    #     self.child_gender_1 = False
    #     self.child_name_2 = False
    #     self.child_gender_2 = False
    #     self.child_name_3 = False
    #     self.child_gender_3 = False
        
    #     if self.children_ShubCreated == '1':
    #         self.child_name_1 = ''
    #         self.child_gender_1 = ''
    #     if self.children_ShubCreated == '2':
    #         self.child_name_2 = ''
    #         self.child_gender_2 = ''
    #     if self.children_ShubCreated == '3':
    #         self.child_name_3 = ''
    #         self.child_gender_3 = ''











# class Child(models.Model):
#     _name = 'employee.child'
#     _description = 'Child Details'

#     name = fields.Char(string='Child Name', required=True)
#     gender = fields.Selection([
#         ('male', 'Male'),
#         ('female', 'Female'),
#         ('other', 'Other')
#     ], string='Gender', required=True)
#     employee_id = fields.Many2one('hr.employee', string='Employee', ondelete='cascade')




# children_ids = fields.One2many('employee.child', 'employee_id', string='Children')

#     @api.onchange('children_ShubCreated')
#     def _onchange_children_ShubCreated(self):
#         if self.children_ShubCreated >= 0:
#             existing_lines = len(self.children_ids)
#             if self.children_ShubCreated > existing_lines:
#                 for _ in range(self.children_ShubCreated - existing_lines):
#                     self.children_ids.new({'name': '', 'gender': 'male'})