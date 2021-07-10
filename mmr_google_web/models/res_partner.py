# -*- coding: utf-8 -*-
from odoo import models, fields
import werkzeug.urls


class ResPartner(models.Model):
    _inherit = "res.partner"

    googlemap_search_key = fields.Char("Google Map Search Key")
    googlemap_zoom = fields.Integer("Google Map Zoom")

    def google_map_img(self, zoom=16, width=298, height=298):
        google_maps_api_key = self.env['website'].get_current_website().google_maps_api_key
        if not google_maps_api_key:
            return False
        if self.googlemap_search_key:
            params = {
                'center': '%s, %s %s, %s' % (self.googlemap_search_key or '', self.city or '', self.zip or '', self.country_id and self.country_id.display_name or ''),
                'size': "%sx%s" % (width, height),
                'zoom': self.googlemap_zoom or zoom,
                'sensor': 'false',
                'key': google_maps_api_key,
            }
        else:
            params = {
                'center': '%s, %s %s, %s' % (self.street or '', self.city or '', self.zip or '', self.country_id and self.country_id.display_name or ''),
                'size': "%sx%s" % (width, height),
                'zoom': self.googlemap_zoom or zoom,
                'sensor': 'false',
                'key': google_maps_api_key,
            }
        return '//maps.googleapis.com/maps/api/staticmap?' + werkzeug.urls.url_encode(params)

    def google_map_link(self, zoom=10):
        return 'https://www.google.com/maps/place/PT.+Multi+Medika+Raharjo/@-6.9824906,110.3893967,15z/data=!4m2!3m1!1s0x0:0x3ca8b2bf3e91f1d6?sa=X&ved=2ahUKEwj854vOvtjxAhUjheYKHaWOC_oQ_BIwEnoECEcQBQ'
