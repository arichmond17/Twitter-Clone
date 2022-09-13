from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

# tables-> models 
# columns -> fields 

class Post(models.Model):
    class Meta(object):
        db_table='post'
    name= models.CharField(
        'Name',blank=False,null=False,max_length=50,default='Abc'
    )
    body=models.CharField(
        'Body',blank=True,null=True,max_length=50,db_index=True,
    )
    created_at=models.DateTimeField(
        'Created_at',blank=True,auto_now_add=True,
    )
    image=CloudinaryField(
        'Image',blank=True,
    )
    likes= models.PositiveIntegerField(
        'like',default=0,blank=True,
    )

    # emails->EmailField
    # urls->urlfield

