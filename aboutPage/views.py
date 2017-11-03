# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.template import Context
from instaMap.models import Post
from django.shortcuts import render
from forms import ContactForm


def show_about(request):
    adventures = Post.objects.filter(image_url__contains='http')
    while len(adventures) < 6:
        adventures.append(adventures[0])
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
        context = Context({
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content,
        })
        content = template.render(context)

        email = EmailMessage(
            "New contact form submission",
            content,
            "Your website" + 'www.critsandcoffee.com',
            ['srwagsta@gmail.com'],
            headers={'Reply-To': contact_email}
        )
        email.send()
        # maybe redirect to a quick loading screen and then back to the home page?
        return redirect('contact')

    context = {
        'form': form_class,
        'page': 'C&C - about',
        'adventure1': adventures[0],
        'adventure2': adventures[1],
        'adventure3': adventures[2],
        'adventure4': adventures[3],
        'adventure5': adventures[4],
        'adventure6': adventures[5],
    }
    return render(request, 'about_page.html', context)
