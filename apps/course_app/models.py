from django.db import models

class Course(models.Model):
    name = models.CharField(max_length =255)
    desc = models.TextField(max_length =100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
