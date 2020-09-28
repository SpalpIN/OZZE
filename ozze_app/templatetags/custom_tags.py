from django import template
from ..models import CoatModel

register = template.Library()

@register.simple_tag
def total_sale_products():
    return CoatModel.objects.filter(sale__gt=0).count()