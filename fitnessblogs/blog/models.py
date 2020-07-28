from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class blogpost(models.Model):
    blog_id = models.AutoField(primary_key = True)
    blog_title = models.CharField(max_length=500)
    blog_head1 = models.CharField(max_length=500)
    blog_cont1 = models.CharField(max_length=5000)
    blog_head2 = models.CharField(max_length=500)
    blog_cont2 = models.CharField(max_length=5000)
    pub_date = models.DateField()
    blog_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)


    def __str__(self):
        return self.blog_title
    

class Post(models.Model):
    post_id = models.AutoField(primary_key = True)
    post_title = models.CharField(max_length=500)
    post_content = models.TextField()
    author = models.CharField(max_length=50)
    slug = models.CharField(max_length=150)
    views = models.IntegerField(default=0)
    pub_date = models.DateTimeField(blank=True)
    image = models.ImageField(upload_to="shop/images")

    def __str__(self):
        return self.post_title


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment + "..." + "by " + self.user.username
        
    
    

