from odoo import models, fields, Command


class AssignAttendeeSessions(models.TransientModel):
    _name = 'assing.attendee.sessions'
    _description = 'Assign Attendee Sessions'

    session_ids = fields.Many2many('session')
    attendee_ids = fields.Many2many('res.partner')

    def action_register_attendees_to_sessions(self):
        for session in self.session_ids:
            if len(session.attendee_ids) + len(self.attendee_ids) <= session.number_of_seats:
                session.write({'attendee_ids': [Command.link(attendee.id) for attendee in self.attendee_ids]})
