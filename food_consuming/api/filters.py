import django_filters
from food_consuming.models import Food, Consume

class FoodFilter(django_filters.FilterSet):
    proteins_min = django_filters.NumberFilter(field_name='proteins', lookup_expr='gte')
    proteins_max = django_filters.NumberFilter(field_name='proteins', lookup_expr='lte')
    calories_min = django_filters.NumberFilter(field_name='calories', lookup_expr='gte')
    calories_max = django_filters.NumberFilter(field_name='calories', lookup_expr='lte')
    fats_min = django_filters.NumberFilter(field_name='fats', lookup_expr='gte')
    fats_max = django_filters.NumberFilter(field_name='fats', lookup_expr='lte')
    carbs_min = django_filters.NumberFilter(field_name='carbs', lookup_expr='gte')
    carbs_max = django_filters.NumberFilter(field_name='carbs', lookup_expr='lte')

    is_expensive = django_filters.BooleanFilter(method='filter_expensive')

    class Meta:
        model = Food
        fields = {
            'name': ['exact', 'icontains'],
            'calories': ['exact', 'gte', 'lte'],
            'carbs': ['exact', 'gte', 'lte'],
            'fats': ['exact', 'gte', 'lte'],
            'price': ['exact', 'gte', 'lte', 'lt'],
        }

    # def filter_expensive(self, queryset, name, value):
    #     if value:
    #         queryset = queryset.filter(price__gte=100)
    #         return queryset
    #     queryset = queryset.filter(price__lt=100)
    #     return queryset