# -*- coding: utf-8 -*-
from odoo import fields, models


class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    certificate_url = fields.Char(
        string="Certificate URL",
        compute="_compute_certificate_url",
        help="Direct link to Odoo's built-in certificate PDF report for this attempt.",
    )
    certificate_organization = fields.Char(
        string="Certificate Organization",
        compute="_compute_certificate_organization",
        help="Organization name used when sharing the certificate to LinkedIn.",
    )
    certificate_organization_id = fields.Char(
        string="LinkedIn Organization ID",
        compute="_compute_certificate_organization",
        help="Your company's LinkedIn Page ID, set in Settings. Empty if not configured.",
    )
    certificate_issue_year = fields.Integer(
        string="Certificate Issue Year",
        compute="_compute_certificate_issue_date",
    )
    certificate_issue_month = fields.Integer(
        string="Certificate Issue Month",
        compute="_compute_certificate_issue_date",
    )

    def _compute_certificate_issue_date(self):
        for rec in self:
            issue_date = rec.write_date or rec.create_date
            if rec.state == 'done' and rec.scoring_success and issue_date:
                rec.certificate_issue_year = issue_date.year
                rec.certificate_issue_month = issue_date.month
            else:
                rec.certificate_issue_year = False
                rec.certificate_issue_month = False

    def _compute_certificate_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for rec in self:
            if rec.state == 'done' and rec.scoring_success:
                rec.certificate_url = f"{base_url}/report/pdf/survey.certification_report/{rec.id}"
            else:
                rec.certificate_url = False

    def _compute_certificate_organization(self):
        for rec in self:
            company = rec.survey_id.company_id if 'company_id' in rec.survey_id._fields else False
            company = company or rec.env.company
            rec.certificate_organization = company.name
            # Optional: only set if the admin configured one in Settings.
            # Left empty (falsy) on purpose when not configured, so the
            # LinkedIn share URL simply omits this parameter — no error.
            rec.certificate_organization_id = company.linkedin_organization_id or False
