from django import template
from django.http import HttpRequest
from django.template import RequestContext

from ..models import MenuItem


register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context: RequestContext, name: str):
    current_path = context['request'].path if 'request' in context and isinstance(context['request'], HttpRequest) \
        else ''

    operating_menu = MenuItem.objects.select_related('menu').filter(menu__name=name).order_by('tree_level')

    menu = []

    for item in operating_menu:
        path = item.path.strip()
        target = '_self'

        url = f'/{item.menu.name}/{path}/'

        tree_list = list(item.tree_level.split('.'))

        menu.append({
            'id': item.pk,
            'url': url,
            'target': target,
            'name': item.name,
            'tree_list': tree_list,
            'highest_level': True if len(tree_list) == 1 else False,
            'active': True if url == current_path else False,
        })

    return {
        'menu': menu,
        'submenu_gen': (item for item in menu if item['tree_list'][:-1] == []),
    }


@register.inclusion_tag('menu.html', takes_context=True)
def draw_submenu(context: RequestContext, t: list):
    menu = context['menu']

    return {
        'menu': menu,
        'submenu_gen': (item for item in menu if item['tree_list'][:-1] == t),
    }
