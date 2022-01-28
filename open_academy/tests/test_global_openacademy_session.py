from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase


class GlobalTestOpenAcademySession(TransactionCase):
    def setUp(self):
        super().setUp()
        self.session = self.env['session']
        self.course_id = self.env.ref('open_academy.course_demo1').id
        self.partner_id = self.env.ref('open_academy.res_partner_jerudiel').id
        self.partner_id_2 = self.env.ref('open_academy.res_partner_open_academy_benito').id
    
    def create_session(self, session_name, session_number_of_seats, session_instructor_id, session_course_id, session_attendee_ids):
        session_id = self.session.create({
            'name': session_name,
            'number_of_seats': session_number_of_seats,
            'instructor_id': session_instructor_id,
            'course_id': session_course_id,
            'attendee_ids': [(6, 0, [session_attendee_ids])],
        })
        return session_id
    
    def test_00_instructor_is_attendee(self):
        with self.assertRaisesRegex(
            ValidationError,
            "Instructor can't be in attendees"
        ):
            self.create_session('test', 1, self.partner_id, self.course_id, self.partner_id)

    def test_01_attendees_greater_number_of_seats(self):
        with self.assertRaisesRegex(
            ValidationError,
            "The test can't have more attendees"
        ):
            self.create_session('test', 0, self.partner_id, self.course_id, self.partner_id_2)
