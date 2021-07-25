from odoo import api, fields, models

class Course (models.Model):
    _name = 'academic.course'

    name = fields.Char("Nama", required=True, size= 100)
    description = fields.Text("Description")
    resposible_id = fields.Many2one(
        comodel_name="res.users",
        string="Responsible",
        required=True
    )