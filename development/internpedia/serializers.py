from rest_framework import serializers
from .models import Company, Internship, Review, Vote, Comment, User
from urllib.parse import unquote  # Use unquote to decode URL

class CustomURLField(serializers.URLField):
    def to_representation(self, value):
        return unquote(super().to_representation(value))

class CompanySerializer(serializers.ModelSerializer):
    company_logo = CustomURLField()
    class Meta:
        model = Company
        fields = '__all__'

class InternshipSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Internship
        fields = '__all__'
        
   # def to_representation(self, instance):
   #     instance.avgNumRating = round(float(instance.avgNumRating), 2)
   #     instance.site = instance.get_site_display()
   #     return super().to_representation(instance)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class VoteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Vote 
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'