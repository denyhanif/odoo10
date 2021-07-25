from odoo import fields,models

class attendee(models.Model):
    _name = "academic.attendee"

    name= fields.Char("Reg Number" , require=True, size=100)
    session_id = fields.Many2one(comodel_name="academic.session", string="Session")
    partner_id = fields.Many2one(comodel_name="res.partner", string="Peserta")
