from odoo import models, fields, Command


class AssignAttendeeSessions(models.TransientModel):
    _name = 'assing.attendee.sessions'
    _description = 'Assign Attendee Sessions'

    session_id = fields.Many2one('session')
    attendee_ids = fields.Many2many('res.partner')

    def add_attendees_session(self):
        self.session_id.write({'attendee_ids': [Command.link(attendee.id) for attendee in self.attendee_ids]})
