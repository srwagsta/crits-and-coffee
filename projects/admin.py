# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Project
from django.contrib import admin
from imagekit.admin import AdminThumbnail


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['proj_name', 'description', 'image_display']
    image_display = AdminThumbnail(image_field='image_thumbnail')
    image_display.short_description = 'Image'
    readonly_fields = ['image_display']


admin.site.register(Project, ProjectAdmin)

