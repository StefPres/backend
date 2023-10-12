from django.shortcuts import render
from rest_framework import viewsets
from .serializers import InternshipSerializer
from .serializers import CompanySerializer
from .models import Internship
from .models import Company 

class InternshipView (viewsets.ModelViewSet):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer

class CompanyView (viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer