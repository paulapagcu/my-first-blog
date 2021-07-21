from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
# Post: name of model which is an object
# Always start class name with uppercase and avoid special characters and whitespace
# models.Model means that Post is a Django Model so Django knows that it should be saved in the database

class Post(models.Model):
    # author - published_date are the object properties
    # the code below defines the properties and their corresponsing types
    # models.ForeignKey: link to another model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # CharField: text with limited num of characters
    title = models.CharField(max_length=200)
    # TextField: long text without a limit
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # methods
    # use lowercase and underscores for method names
    # methods often return something as seen in __str__(self), which returns the title
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title