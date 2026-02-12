from django.db import models

# Create your models here.
# Create your models here.
class ContactSubmission(models.Model):
    name= models.CharField(max_length=100)
    email=models. EmailField()
    created_at=models.DateTimeField(auto_now_add=True)
    message=models. TextField()

def __str__(self):
    return self.name