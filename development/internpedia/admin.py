from django.contrib import admin
from .models import Internship
from .models import Company

class InternshipAdmin(admin.ModelAdmin):
    list_display = ('company','title', 'description', 'site', 'rating','location','paid','qualifications')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_logo', 'industry', 'description', 'website')

admin.site.register(Internship, InternshipAdmin)
admin.site.register(Company, CompanyAdmin)