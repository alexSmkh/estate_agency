from django.contrib import admin

from .models import Flat


class PriceListFilter(admin.SimpleListFilter):
    title = 'Стоимость квартиры(₽)'
    parameter_name = 'flat_price'

    def lookups(self, request, model_admin):
        return(
            ('<1m', 'менее 1.000.000'),
            ('1-2m', 'от 1.000.000 до 2.000.000'),
            ('2-5m', 'от 2.000.000 до 5.000.000'),
            ('5-10m', 'от 5.000.000 до 10.000.000'),
            ('10-20m', 'от 10.000.000 до 20.000.000'),
            ('>20m', 'от 20.000.000 и более'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == '<1m':
            return queryset.filter(price__lt=1000000)
        elif value =='1-2m':
            return queryset.filter(price__gte=1000000, price__lt=2000000)
        elif value =='2-5m':
            return queryset.filter(price__gte=2000000, price__lt=5000000)
        elif value =='5-10m':
            return queryset.filter(price__gte=5000000, price__lt=10000000)
        elif value =='10-20m':
            return queryset.filter(price__gte=10000000, price__lt=20000000)
        elif value =='>20m':
            return queryset.filter(price__gte=20000000)


class LivingAreaListFilter(admin.SimpleListFilter):
    title = 'Жилая площадь(м²)'
    parameter_name = 'living_area'

    def lookups(self, request, model_admin):
        return(
            ('<40', 'меньше чем 40'),
            ('41-60', 'от 41 до 60'),
            ('61-80', 'от 61 до 80'),
            ('81-100', 'от 81 до 100'),
            ('>100', '101 и более'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == '<40':
            return queryset.filter(living_area__lt=40)
        elif value =='41-60':
            return queryset.filter(living_area__gte=41, living_area__lte=60)
        elif value =='61-80':
            return queryset.filter(living_area__gte=61, living_area__lte=80)
        elif value =='81-100':
            return queryset.filter(living_area__gte=81, living_area__lte=100)
        elif value =='>100':
            return queryset.filter(living_area__gt=100)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'town', 'address')
    readonly_fields = ('created_at',)
    list_display = (
        'address', 'price', 'new_building', 'construction_year', 'town'
    )
    list_editable = ('new_building',)
    list_filter = (
        'created_at',
        'new_building',
        'active',
        'has_balcony',
        'rooms_number',
        LivingAreaListFilter,
        PriceListFilter
    )
