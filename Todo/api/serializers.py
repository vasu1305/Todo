from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Todo

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'