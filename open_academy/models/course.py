from odoo import models, fields


class Course(models.Model):
    _name = 'course'
    _description = 'Course'

    title = fields.Char(required=True)
    description = fields.Text()
    responsible_user_id = fields.Many2one("res.users")
    session_ids = fields.One2many("session", "course_id")

    _sql_constraints = [
        ('description_and_title_are_differents', 'CHECK (title <> description)', 'Title and description must be differents'),
        ('title_unique', 'UNIQUE (title)', 'Title must be unique'),
    ]
