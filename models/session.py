from odoo import fields,models

class Session(models.Model):
    _name = "academic.session"

    name = fields.Char("name", required= True, size = 100)

    course_id = fields.Many2one( comodel_name="academic.course", string="Course")
    instructor_id = fields.Many2one(comodel_name="res.partner", string="Instructor")
    start_date = fields.Datetime("start date")
    duration = fields.Integer("Duration")
    seats = fields.Integer("seats")
    active = fields.Boolean("Is Active", default= True)

    # relasi
    attende_ids = fields.One2many(comodel_name="academic.attendee",string="attende", inverse_name="session_id")