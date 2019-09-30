from django.db import models

# Create your models here.

class Category(models.Model):
    name =models.CharField(max_length=255)

class REST(models.Model):
    title = models.CharField(max_length=255)
    short_content = models.CharField(max_length=255)
    full_content = models.CharField(max_length=255)
    category =models.ForeignKey("Category" ,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.short_content} {self.full_content}"

