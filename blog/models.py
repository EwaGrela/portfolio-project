from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] + "..."


    def created_short(self):
        return self.created.strftime('%e %b %Y')



