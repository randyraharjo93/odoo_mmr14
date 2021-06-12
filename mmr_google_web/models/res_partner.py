# -*- coding: utf-8 -*-
from openerp import api, fields, models, _
import base64
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from dateutil.relativedelta import relativedelta
from datetime import datetime, date, timedelta
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = "res.partner"

    def google_map_img(self, zoom=8, width=298, height=298):
        return False

    def google_map_link(self, zoom=10):
        return 'https://www.google.com/search?safe=strict&sz=16&q=mmr%20semarang&sa=X&ved=2ahUKEwi-3pjA4JLxAhWYT30KHQ_0Az0QvS4wAHoECAMQKw&biw=1294&bih=637&dpr=1&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&tbm=lcl&rflfq=1&num=10&rldimm=4370939972821316054&lqi=CgxtbXIgc2VtYXJhbmdIwOqi7purgIAIWhIQABgBIgxtbXIgc2VtYXJhbmeSARBjb3Jwb3JhdGVfb2ZmaWNlqgELEAEqByIDbW1yKCY&rlst=f#rlfi=hd:;si:4370939972821316054,l,CgxtbXIgc2VtYXJhbmdIwOqi7purgIAIWhIQABgBIgxtbXIgc2VtYXJhbmeSARBjb3Jwb3JhdGVfb2ZmaWNlqgELEAEqByIDbW1yKCY;mv:[[-6.9626785,110.4687417],[-7.1193903999999995,110.3405669]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2'
