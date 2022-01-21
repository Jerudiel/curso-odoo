from odoo import models, fields


class AssignAttendeeSessions(models.TransientModel):
    _name = 'assing.attendee.sessions'
    _description = 'Assign Attendee Sessions'

    session_id = fields.Many2one('session')
    attendee_ids = fields.Many2many('res.partner')
