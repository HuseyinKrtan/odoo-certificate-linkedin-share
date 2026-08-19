# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    linkedin_organization_id = fields.Char(
        related='company_id.linkedin_organization_id',
        readonly=False,
        string="LinkedIn Organization ID",
    )
