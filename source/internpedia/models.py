from django.db import models

#Our model for individual companies, containing info relevant to the company
class Company(models.Model): 
    company_logo = models.ImageField()
    industry = models.CharField()
    description = models.TextField()


# Our model for individual internship listings
class Internship(models.Model):
    title = models.CharField()
    role = models.CharField()
    remote = models.BooleanField() #True if Remote, #False if On-Site
    company = models.ForeignKey(Company, on_delete=models.CASCADE) # if a company is deleted from our website, all internships under that company will also be deleted
    description = models.TextField()

#Our model for individual reviews.
class Review(models.Model):
    review_text = models.TextField()
