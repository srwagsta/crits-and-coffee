# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from instaMap.models import Post
from django.shortcuts import render


def show_landing(request):
    instance_posts = Post.objects.filter(tags__contains='foodie')
    if instance_posts > 0:
        foodie_post = instance_posts[0]
    else:
        foodie_post = Post.objects.get(pk=1)

    instance_posts = Post.objects.filter(tags__contains='cycling')
    if instance_posts > 0:
        cycling_post = instance_posts[0]
    else:
        cycling_post = Post.objects.get(pk=1)

    context = {
        'page': 'crits & coffee',
        'foodie_post': foodie_post,
        'cycling_post': cycling_post,
        'professional_pic': 'https://media.licdn.com/mpr/mpr/shrinknp_400_400/AAIA_wDGAAAAAQAAAAAAAA3iAAAAJGVkYTg3MzZlLTU5YjktNGI0ZS04ZWJkLTg4NjgxYWIyNjZhMg.jpg',
    }
    return render(request, 'landing_page.html', context)
    # We can add an argument if we want to display something dynamically

