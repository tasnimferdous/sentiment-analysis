from django.db import models

# Create your models here.

class Sentence(models.Model):
    text = models.CharField(max_length=512)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
