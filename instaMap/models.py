# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models


class Post(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.

    content = models.TextField(default='None')
    id_code = models.TextField(default='None')
    tags = models.TextField(default='None')
    link = models.TextField(default='None')
    image_url = models.TextField(default='None')
    loc_name = models.TextField(default='None')

    # GeoDjango-specific: a geometry field (PointField)
    loc_point = models.PointField(srid=4326, default='SRID=4326;POINT(43.065019 -87.878286)')

    # Returns the string representation of the model.
    def __str__(self):              # __unicode__ on Python 2
        return self.loc_name
