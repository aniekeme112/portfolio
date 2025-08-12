from rest_framework import serializers
from .models import FeaturedProject

class FeaturedProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedProject
        fields = '__all__'
