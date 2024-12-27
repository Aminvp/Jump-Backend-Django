from .models import Brand, Mobile
from django.db.models import F, Q


def all_brands_not_in_korea_china():
    query = Brand.objects.exclude(nationality="China").exclude(nationality="Korea")
    return query


def some_brand_mobiles(*brand_names):
    if brand_names:
            return Mobile.objects.filter(brand__name__in=brand_names)
    else:
        return Mobile.objects.all()


def mobiles_brand_nation_equals_made_in():
    query = Mobile.objects.filter(brand__nationality=F('made_in'))
    return query
