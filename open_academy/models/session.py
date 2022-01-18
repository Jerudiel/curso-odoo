from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Session(models.Model):
    _name = 'session'
    _description = 'Session'

    name = fields.Char()
    start_date = fields.Datetime(default=lambda self: fields.Date.today())
    duration = fields.Float()
    number_of_seats = fields.Integer(default=1)
    instructor_id = fields.Many2one(
        "res.partner", domain="['|',('is_instructor','=',True),('category_id.name','like','Teacher')]")
    course_id = fields.Many2one("course", required=True)
    attendee_ids = fields.Many2many("res.partner")
    percentage_of_taken_seats = fields.Integer(compute='_compute_percentage_of_taken_seats')
    active = fields.Boolean(default=True)
    antiquity_of_the_session = fields.Selection(
        selection=[('recently', 'Recently'), ('old', 'Old'), ('normal', 'Normal')],
        compute='_compute_antiquity_of_the_session', default='normal')
    attendee_count = fields.Integer(store=True, compute='_compute_attendee_count')

    @api.depends('number_of_seats', 'attendee_ids')
    def _compute_percentage_of_taken_seats(self):
        for record in self:
            percentage = int((len(record.attendee_ids)*100)/record.number_of_seats)
            record.percentage_of_taken_seats = percentage if record.number_of_seats > 0 else 0

    @api.onchange('number_of_seats', 'attendee_ids')
    def _onchange_number_of_seats_and_attendee_ids(self):
        title = ""
        message = ""
        if self.number_of_seats < 0:
            title = "Problem in number of seats"
            message = "The number of seats must be positive"
        elif len(self.attendee_ids) > self.number_of_seats:
            title = "Problem in number of attendees"
            message = "The number of attendees is more than number of seats available"
        return {'warning': {'title': title, 'message': message}}

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_is_not_in_attendees(self):
        for record in self:
            if record.instructor_id in record.attendee_ids:
                raise ValidationError(_("Instructor can't be in attendees"))

    @api.depends('start_date')
    def _compute_antiquity_of_the_session(self):
        for record in self:
            now_date = fields.Datetime.now()
            session_date = record.start_date
            days_to_now = (now_date - session_date).days
            if days_to_now < 5:
                record.antiquity_of_the_session = "recently"
            elif days_to_now > 15:
                record.antiquity_of_the_session = "old"
            else:
                record.antiquity_of_the_session = "normal"

    @api.depends('attendee_ids')
    def _compute_attendee_count(self):
        for record in self:
            record.attendee_count = len(record.attendee_ids)
