from django.db import models

# Create your models here.
class Author(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    notes=models.TextField(max_length=255)
    craeted_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)




class Book(models.Model):
    title=models.CharField(max_length=45)
    description=models.TextField(max_length=255)
    authors=models.ManyToManyField(Author,related_name='books')
    craeted_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
    
