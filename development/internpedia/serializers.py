from rest_framework import serializers
from .models import Company, Internship, Review

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        ## TODO



class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        ## TODO

        

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        ## TODO

