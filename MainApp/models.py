from django.db import models

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)


    # this defines what we want to specifically return, user defined, no jib jab
    def __str__(self):
        return self.text

# this is creating an FK in connection to Topic, inner join 
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        #this overrides the default of just adding an 's' 
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."
    
