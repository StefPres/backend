from django.shortcuts import render
from rest_framework import viewsets
from .serializers import InternshipSerializer
from.serializers import VoteSerializer
from .serializers import CompanySerializer, ReviewSerializer
from .models import Internship, Vote
from .models import Company, Review

class InternshipView (viewsets.ModelViewSet):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer

class CompanyView (viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class VoteView(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
