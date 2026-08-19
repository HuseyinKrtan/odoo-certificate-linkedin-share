# -*- coding: utf-8 -*-
from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    linkedin_organization_id = fields.Char(
        string="LinkedIn Organization ID",
        help="Your company's LinkedIn Page ID. When set, certificate shares "
             "will link directly to this page on LinkedIn. If left empty, "
             "the company name (organizationName) is used instead — no "
             "error will occur either way.",
    )
