from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError
class leave_management(models.Model):
    _name = 'leave.management'
    _description = 'Custom Leave Management'

    name = fields.Char(string='Leave Name')
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    manager_id = fields.Many2one('hr.employee', string='Manager', compute='_compute_manager', store=True)
    leave_type = fields.Selection([('sick', 'Sick Leave'), ('vacation', 'Vacation Leave')], string='Leave Type', required=True)
    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date('End Date', required=True)
    reason = fields.Text('Reason for Leave', required=True)
    state = fields.Selection([('draft', 'Draft'), ('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')],
                             default='draft', string='Status', track_visibility='onchange')
    user_id = fields.Many2one('res.users', 'Current User', compute='_get_current_user')

    def _get_current_user(self):
     self.user_id = self.env.uid

    @api.depends('employee_id')
    def _compute_manager(self):
        for record in self:
            record.manager_id = record.employee_id.parent_id

    def action_request_leave(self):
        self.state = 'pending'
        self.name = self._create_leave_name()

    def action_approve_leave(self):
        get_logged_in_user = self.env.user
        if self.employee_id.name == get_logged_in_user.name:
            raise ValidationError("You cannot approve your own leave request")
        self.state = 'approved'

    def action_reject_leave(self):
        self.state = 'rejected'

    def _create_leave_name(self):
        month_year = datetime.now().strftime('%m%Y')
        employee_name = self.employee_id.name.replace(' ', '').upper()
        return f"{month_year}-{employee_name}"