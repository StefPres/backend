from django.shortcuts import get_object_or_404
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
            results = Internship.objects.filter(
                Q(title__icontains=query) |
                Q(company__title__icontains=query) |
                Q(description__icontains=query)
            ).select_related('company')  # Use select_related to fetch company details in a single query

            serialized_results = InternshipSerializer(results, many=True).data

            return Response(serialized_results, status=status.HTTP_200_OK)
        
        all_internships = Internship.objects.all().select_related('company')
        serialized_all_internships = InternshipSerializer(all_internships, many=True).data

        return Response(serialized_all_internships, status=status.HTTP_200_OK)

class CompanyDetailView(APIView):
    def get(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        serializer = CompanySerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)