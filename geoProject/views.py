from __future__ import unicode_literals
from django.shortcuts import render


def custom_404(request):
    return render(request, 'base_templates/404.html', {}, status=404)