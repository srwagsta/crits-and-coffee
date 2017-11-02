# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from instaMap.models import Post
from django.shortcuts import render


def show_about(request):
    adventures = Post.objects.filter(image_url__contains='http')
    while len(adventures) < 6:
        adventures.append(adventures[0])
    context = {
        'page': 'C&C - about',
        'adventure1': adventures[0],
        'adventure2': adventures[1],
        'adventure3': adventures[2],
        'adventure4': adventures[3],
        'adventure5': adventures[4],
        'adventure6': adventures[5],
    }
    return render(request, 'about_page.html', context)
