from django.shortcuts import render

from .service import database_debug


@database_debug
def menu(request, menu_url, path_url):
    return render(request, 'block.html')

