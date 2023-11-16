from django.shortcuts import render
from rest_framework import viewsets
from .serializers import InternshipSerializer
from.serializers import VoteSerializer
from .serializers import CompanySerializer, ReviewSerializer, UserSerializer
from .models import Internship, Vote, User
from .models import Company, Review
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

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

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class InternshipSearchView(APIView):
    def get(self, request):
        query = request.query_params.get('query', '').strip()
        if query:
            # Perform a case-insensitive search on multiple fields using Q objects
            results = Internship.objects.filter(
                Q(title__icontains=query) |
                Q(company__title__icontains=query) |
                Q(description__icontains=query)
            )
            serializer = InternshipSerializer(results, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        all_internships = Internship.objects.all()
        serializer = InternshipSerializer(all_internships, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)