from odoo import http


class DashboardController(http.Controller):
    """This method is to avoid show dashboard error: edit_custom() missing argument: custom_id
    when dashboard view changes"""
    @http.route('/web/view/edit_custom', type='json', auth="user")
    def edit_custom(self, arch):
        return {'result': True}
