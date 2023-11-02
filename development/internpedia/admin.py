from django.contrib import admin
from .models import Internship, Company, Review, Vote, User

class InternshipAdmin(admin.ModelAdmin):
    list_display = ('company','title', 'description', 'rating','location','paid')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_logo', 'industry', 'description', 'website')

class ReviewAdmin(admin.ModelAdmin):
    def downvote_count(self):
        return self.votes.filter(voted=False).count()
    
    def upvote_count(self):
        return self.votes.filter(voted=True).count()
    
    def get_upvotes(self, obj):
        return obj.upvote_count()

    def get_downvotes(self, obj):
        return obj.downvote_count()

    list_display = ('internship', 'review_text', 'site', 'startDate', 'endDate', 'rating','paid', 'hourly_wage', 'yearly_salary', 'get_upvotes','get_downvotes')

class VoteAdmin(admin.ModelAdmin):
    list_display = ('review', 'voted')

class UserAdmin(admin.ModelAdmin):
    
    def display_reviews(self, obj):
        return ", ".join([str(review) for review in obj.reviews.all()])
    
    list_display = ('firstname','lastname','username','email','password', 'confirmPass','display_reviews')

admin.site.register(Internship, InternshipAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(User, UserAdmin)