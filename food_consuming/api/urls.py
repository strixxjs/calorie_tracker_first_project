from django.urls import include, path
from rest_framework import routers
from food_consuming.api import views
from .views import FoodViewSet
# from path.to.your.registration_view import RegisterView


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'foods', views.FoodViewSet, basename='foods')
router.register(r'consumes', views.ConsumeViewSet)
# router.register(r'foods', FoodViewSet, basename='foods')

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/register/', RegisterView.as_view(), name='register'),
]