# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models, _
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class ProjectProject(models.Model):
    _inherit = "project.project"

    mis_report_template_id = fields.Many2one('mis.report', string="Mis Report Template")
    mis_report_instance_id = fields.Many2one('mis.report.instance', string="Mis Report")

    def generate_monthly_dates(self):
        result = []
        current_date = self.date_start.replace(day=1)
        end_date = self.date.replace(day=1)
        end_date = end_date.replace(month=self.date.month + 1)

        while current_date < end_date or current_date == end_date:
            result.append(current_date)
            current_date += relativedelta(months=1)
        return result

    def auto_create_mis_instance(self):
        instance_id = self.mis_report_instance_id.create({
            'name': _('Project: %s') % self.name,
            'report_id': self.mis_report_template_id.id,
            'comparison_mode': True,
            'date': self.date_start,
            'analytic_account_id': self.analytic_account_id.id
        })

        months_range = self.generate_monthly_dates()

        count_month = 0
        for month in months_range:
            period_id = instance_id.period_ids.create({
                'report_instance_id': instance_id.id,
                'name': '%s/%s' % (month.strftime("%m"), month.strftime("%Y")),
                'source': 'actuals',
                'mode': 'relative',
                'type': 'm',
                'offset': count_month,
                'duration': 1,
            })
            count_month += 1
        self.mis_report_instance_id = instance_id
