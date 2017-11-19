# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from projects.models import Project
from django.shortcuts import render


def show_projects(request):
    context = {
        'page': 'C&C - Projects',
        'projects': Project.objects.all()
    }
    return render(request, 'project_page.html', context)
