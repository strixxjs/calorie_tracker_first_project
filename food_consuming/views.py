from django.shortcuts import render, redirect
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .api.serializers import ConsumeSerializer, FoodSerializer
from .models import Food, Consume
from django.http import HttpResponse


from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'carbs', 'proteins', 'fats', 'price']

class ConsumeViewSet(viewsets.ModelViewSet):
    queryset = Consume.objects.all()
    serializer_class = ConsumeSerializer
    permission_classes = [IsAuthenticated]


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foods'] = Food.objects.all()
        context['consumed_food'] = Consume.objects.filter(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        food_consumed = request.POST['food_consumed']
        food = Food.objects.filter(name=food_consumed).first()
        user = request.user

        consume = Consume(user=user, food=food)
        consume.save()
        return redirect('index')


class DeleteView(TemplateView):
    template_name = 'delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consumed_food'] = Consume.objects.filter(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        consumed_food = Consume.objects.get(id=kwargs['id'])
        consumed_food.delete()
        return redirect('index')