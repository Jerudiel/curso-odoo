from odoo import models, fields


class Session(models.Model):
    _name = 'session'
    _description = 'Session'

    name = fields.Char()
    start_date = fields.Datetime()
    duration = fields.Float()
    number_of_seats = fields.Integer()
    instructor_id = fields.Many2one("res.partner", domain="['|',('is_instructor','=',True),('category_id.name','like','Teacher')]")
    course_id = fields.Many2one("course", required=True)
    attendee_ids = fields.Many2many("res.partner")
