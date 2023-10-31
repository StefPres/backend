from django.contrib import admin
from .models import Internship
from .models import Company
from .models import Review
from .models import Vote

class InternshipAdmin(admin.ModelAdmin):
    list_display = ('company','title', 'description', 'site', 'rating','location','paid','qualifications')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_logo', 'industry', 'description', 'website')

class ReviewAdmin(admin.ModelAdmin):
    def downvote_count(self):
        return self.votes.filter(voted=False).count()
    
    def upvote_count(self):
        return self.votes.filter(voted=True).count()
    
    def get_upvotes(self, obj):
        return obj.upvote_count()

    def get_downvotes(self, obj):
        return obj.downvote_count()

    get_downvotes.short_description = 'Downvotes'

    list_display = ('internship', 'review_text', 'startDate', 'endDate', 'rating','get_upvotes','get_downvotes')

class VoteAdmin(admin.ModelAdmin):
    list_display = ('review', 'voted')


admin.site.register(Internship, InternshipAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Vote, VoteAdmin)