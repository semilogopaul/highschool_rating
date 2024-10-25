from django.shortcuts import render
from django.http import JsonResponse
from .models import HighSchool, Review
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def list_highschools(request):
    if request.method == 'GET':
        highschools = list(HighSchool.objects.values())
        return JsonResponse(highschools, safe=False)

@csrf_exempt
def add_highschool(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        highschool, created = HighSchool.objects.get_or_create(
            name=data['name'],
            state=data['state'],
            city=data['city']
        )
        return JsonResponse({'id': highschool.id, 'created': created})

@csrf_exempt
def add_review(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        highschool = HighSchool.objects.get(id=data['highschool_id'])
        review = Review.objects.create(
            highschool=highschool,
            rating=data['rating'],
            review_text=data['review_text']
        )
        return JsonResponse({'id': review.id})
