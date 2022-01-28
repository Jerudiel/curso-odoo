from psycopg2.errors import CheckViolation
from psycopg2.errors import UniqueViolation

from odoo.tests.common import TransactionCase
from odoo.tools import mute_logger


class GloabalTestOpenAcademy(TransactionCase):
    def setUp(self):
        super().setUp()
        self.course = self.env['course']
    
    def create_course(self, course_title, course_description, course_responsible_user_id):
        # Create a course with parameters received
        course_id = self.course.create({
            'title': course_title,
            'description': course_description,
            'responsible_user_id': course_responsible_user_id,
        })
        return course_id

    @mute_logger('odoo.sql_db')
    def test_00_same_name_description(self):
        with self.assertRaisesRegex(
            CheckViolation,
            'new row for relation "course" violates check constraint "course_description_and_title_are_differents"'
        ):
            self.create_course('test', 'test', None)

    @mute_logger('odoo.sql_db')
    def test_01_same_name_description(self):
        with self.assertRaisesRegex(
            UniqueViolation,
            'duplicate key value violates unique constraint "course_title_unique"'
        ):
            self.create_course('test', 'test_description_00', None)
            self.create_course('test', 'test_description_01', None)

    def test_02_duplicate_course(self):
        course = self.env.ref('open_academy.course_demo1')
        copy_course = course.copy()
        new_course = self.course.search([('title', '=', copy_course[0]['title'])])
        self.assertRecordValues(new_course, [{'title': f'Copy of {course.title}'}])
