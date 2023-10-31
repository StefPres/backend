from django.db import models

#Our model for individual companies, containing info relevant to the company
class Company(models.Model): 
    title = models.CharField(max_length=200)
    company_logo = models.ImageField()
    industry = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField()


# Our model for individual internship listings
class Internship(models.Model):
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE) # if a company is deleted from our website, all internships under that company will also be deleted
    description = models.TextField()
    location = models.CharField(max_length=100)
    paid = models.BooleanField()
    salary = models.DecimalField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    qualifications = models.TextField()

    On_Site = 'On-Site'
    Remote = 'Remote'
    Hybrid = 'Hybrid'
    
    class places(models.TextChoices):
        On_Site = 'On-Site'
        Remote = 'Remote'
        Hybrid = 'Hybrid'
    
    site = models.TextField(choices=places.choices)

    #note: remember we want to recommend TRENDING internships or reviews
    #what are things we can keep track of to signify that an internship or review is trending?

#Our model for individual reviews.
class Review(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    review_text = models.TextField()
    startDate = models.DateField(auto_now_add=True)
    endDate = models.DateField(auto_now_add=True)
    returnOffer = models.BooleanField()


    onestar = 1
    twostar = 2
    threestar = 3
    fourstar = 4
    fivestar = 5

    class starRating(models.IntegerChoices):
        onestar = 1
        twostar = 2
        threestar = 3
        fourstar = 4
        fivestar = 5
    
    rating = models.IntegerField(choices=starRating.choices,default=threestar)
    votes = models.ManyToManyField('Vote', related_name='reviews')

    def upvote_count(self):
        return self.votes.filter(voted=True).count()
    
    def downvote_count(self):
        return self.votes.filter(voted=False).count()


class Vote(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    voted = models.BooleanField(default=False)
    
    def toggle_vote(self):
        self.voted = not self.voted
        self.save()



class Comment(models.Model):
    post = models.ForeignKey(Review,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
