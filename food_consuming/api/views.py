from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets , permissions, filters
from food_consuming.api.serializers import UserSerializer, FoodSerializer, ConsumeSerializer
from food_consuming.models import Food, Consume
from food_consuming.api.filters import FoodFilter

class FoodViewSet(viewsets.ModelViewSet):

    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # filterset_fields = [
    #     "name",
    #     "calories",
    #     "carbs",
    #     "proteins",
    #     "fats",
    #     "price",
    # ]

    filterset_class = FoodFilter

    search_fields = ["name"]

    ordering_fields = ["name", "calories", "carbs", "proteins", "fats", "price"]

    ordering = ["name"]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ConsumeViewSet(viewsets.ModelViewSet):
    queryset = Consume.objects.all()
    serializer_class = ConsumeSerializer
    permission_classes = [permissions.IsAuthenticated]


# class FoodViewSet(viewsets.ModelViewSet):
#     queryset = Food.objects.all()
#     serializer_class = FoodSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = [
#         'name', 'carbs', 'proteins', 'fats'
#     ]



# class FoodViewSet(viewsets.ModelViewSet):
#     queryset = Food.objects.all()
#     serializer_class = FoodSerializer
#     permission_classes = [permissions.IsAuthenticated]
