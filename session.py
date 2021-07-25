from odoo import fields,models

class Session(models.Model):
    _name = "academic.session"

    name = fields.Char("name", required= True, size = 100)