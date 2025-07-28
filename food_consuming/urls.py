from django.urls import path
from food_consuming import views
from django.urls import path, include

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('delete/<int:id>/', views.DeleteView.as_view(), name="delete"),
    path('api/food_consuming/', include('food_consuming.api.urls')),
]