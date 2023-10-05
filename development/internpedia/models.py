from django.db import models

#Our model for individual companies, containing info relevant to the company
class Company(models.Model): 
    company_logo = models.ImageField()
    industry = models.CharField(max_length=100)
    description = models.TextField()


# Our model for individual internship listings
class Internship(models.Model):
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE) # if a company is deleted from our website, all internships under that company will also be deleted
    description = models.TextField()

    #note: remember we want to recommend TRENDING internships or reviews
    #what are things we can keep track of to signify that an internship or review is trending?

#Our model for individual reviews.
class Review(models.Model):
    review_text = models.TextField()
