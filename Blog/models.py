from django.db import models
from django.utils import timezone

# Create your models here.
class Blogs(models.Model):
    BLOG_TYPE=(
        ('SPORTS','SPORTS'),
        ('TRAVEL','TRAVEL'),
        ('POLTICIS','POLITICS'),
        ('NATIONAL BLOG','NATIONAL BLOG'),
    )
    blog_name=models.CharField(null=False,blank=True, max_length=100)
    text=models.TextField(blank=True,null=True)
    blog_img=models.ImageField(upload_to='blogImg/',null=True,blank=True)
    blog_type=models.CharField(choices=BLOG_TYPE,null=False,max_length=18)
    created_at=models.DateTimeField(default=timezone.now)
    updated_time=models.DateTimeField(default=timezone.now)



    def __str__(self):
        return f"{self.blog_name}-{self.text[:20]}"
