# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from instaMap.models import Post
from django.contrib.gis.geoip2 import GeoIP2


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def show_map(request):
    client_ip = get_client_ip(request)
    # client_ip = '74.120.152.136'  # This line will have to be remove when it goes live
    client_pnt = GeoIP2().geos(client_ip)
    context = {
        'client_lat': client_pnt.y,
        'client_lng': client_pnt.x,
        'page': 'C&C - Travel',
        'posts': Post.objects.all(),
    }
    return render(request, 'instamap_page.html', context)
