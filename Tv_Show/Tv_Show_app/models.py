from django.db import models

# Create your models here.
class showsManager(models.Manager):
    def show_validator(self,postData):
        errors={}
    
        if not postData['title']:
            errors['title_empty']="Title is Empty"
        elif len(postData['title'])<2:
            errors['title_len']='Title must be more than 2 characters'
        
        if not postData['network']:
            errors['network_empty']='Network is Empty'
        elif len (postData['network'])<3:
            errors['network_len']="Network must be more than 3 characters"


        if not postData['description']:
            errors['description_empty']='Description is Empty'
        elif len (postData['description'])<10:
            errors['description_len']="Description must be more than 10 characters"
                
        return errors

    def edit_validator(self,postData):
        errors={}
    
        if not postData['title']:
            errors['title_empty']="Title is Empty"
        elif len(postData['title'])<2:
            errors['title_len']='Title must be more than 2 characters'
        
        if not postData['network']:
            errors['network_empty']='Network is Empty'
        elif len (postData['network'])<3:
            errors['network_len']="Network must be more than 3 characters"


        if not postData['description']:
            errors['description_empty']='Description is Empty'
        elif len (postData['description'])<10:
            errors['description_len']="Description must be more than 10 characters"
                
        return errors
        
        

class Shows(models.Model):
    title=models.CharField(max_length=45)
    network=models.CharField(max_length=45)
    release_date=models.DateField()
    description=models.TextField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=showsManager()

    def __str__(self):
        return f"{self.title} {self.network}"