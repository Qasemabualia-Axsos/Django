from django.db import models

# Create your models here.
class Users(models.Model):
    Name=models.CharField(max_length=45)
    Email=models.EmailField(max_length=255)
    Age=models.IntegerField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.Name} {self.Email}"