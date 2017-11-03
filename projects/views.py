# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def show_projects(request):
    return render(request, 'project_page.html')