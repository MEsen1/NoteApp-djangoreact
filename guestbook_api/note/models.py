from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField();
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title} - {self.date_created}'