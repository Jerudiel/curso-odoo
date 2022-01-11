from odoo import models, fields


class Course(models.Model):
    _name = 'course'
    _description = 'Course'

    title = fields.Char(required=True)
    description = fields.Text()
    responsible_user_id = fields.Many2one("res.users")
    session_ids = fields.One2many("session", "course_id")
