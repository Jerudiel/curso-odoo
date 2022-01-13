from odoo import models, fields, api


class Session(models.Model):
    _name = 'session'
    _description = 'Session'

    name = fields.Char()
    start_date = fields.Datetime(default=lambda self: fields.Date.today()) 
    duration = fields.Float()
    number_of_seats = fields.Integer()
    instructor_id = fields.Many2one("res.partner", domain="['|',('is_instructor','=',True),('category_id.name','like','Teacher')]")
    course_id = fields.Many2one("course", required=True)
    attendee_ids = fields.Many2many("res.partner")
    percentage_of_taken_seats = fields.Integer(compute='_compute_percentage_of_taken_seats')
    active = fields.Boolean(default=True)

    @api.depends('number_of_seats','attendee_ids')
    def _compute_percentage_of_taken_seats(self):
        for record in self:
            record.percentage_of_taken_seats = int((len(record.attendee_ids)*100)/record.number_of_seats) if record.number_of_seats > 0 else 0
    
    @api.onchange('number_of_seats','attendee_ids')
    def _onchange_number_of_seats_and_attendee_ids(self):
        if self.number_of_seats < 0:
            return {'warning': {
            'title': "Problem in number of seats",
            'message': "The number of seats must be positive",}}
        elif len(self.attendee_ids) > self.number_of_seats:
            return {'warning': {
            'title': "Problem in number of attendees",
            'message': "The number of attendees is more than number of seats available",}}
