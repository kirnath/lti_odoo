# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.http import Response
from datetime import datetime
import json
class LeaveManagement(http.Controller):

    @http.route('/leave_management', auth='public', methods=['POST'], csrf=False)
    def create_leave(self, **kw):
        employee_id = int(kw.get('employee_id'))
        leave_type = kw.get('leave_type')
        start_date = kw.get('start_date')
        end_date = kw.get('end_date')
        reason = kw.get('reason')

        leave_record = request.env['leave.management'].create({
            'employee_id': employee_id,
            'leave_type': leave_type,
            'start_date': start_date,
            'end_date': end_date,
            'reason': reason,
        })
        
        leave_record.action_request_leave()
        
        return {"status": "success", "leave_name": leave_record.name}

    @http.route('/leave_management/<int:leave_id>/update_status', auth='public', methods=['PUT'], csrf=False)
    def update_leave_status(self, leave_id, **kw):
        leave_record = request.env['leave.management'].browse(leave_id)
        if leave_record.exists():
            new_status = kw.get('status')
            if new_status in ['pending', 'approved', 'rejected']:
                if new_status == 'approved':
                    leave_record.action_approve_leave()
                elif new_status == 'rejected':
                    leave_record.action_reject_leave()
                else:
                    leave_record.state = 'pending'
                return {"status": "success", "message": f"Leave status updated to {new_status}"}
            else:
                return {"status": "error", "message": "Invalid status"}
        return {"status": "error", "message": "Leave record not found"}

    @http.route('/leave_management/all', auth='public', methods=['GET'], csrf=False)
    def get_all_leaves(self, **kw):
        leaves = request.env['leave.management'].search([])
        leave_data = []
        for leave in leaves:
            leave_data.append({
                'leave_name': leave.name,
                'employee_id': leave.employee_id.name,
                'leave_type': leave.leave_type,
                'start_date': leave.start_date.strftime('%Y-%m-%d'),
                'end_date': leave.end_date.strftime('%Y-%m-%d'),
                'status': leave.state,
                'reason': leave.reason,
            })
        response_data = {
        "status": "success",
        "data": leave_data
        }
        return Response(
        json.dumps(response_data), 
        content_type='application/json; charset=utf-8'
    )
