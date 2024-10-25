from rest_framework import serializers
from .models import HighSchool, Review

class HighSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighSchool
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
