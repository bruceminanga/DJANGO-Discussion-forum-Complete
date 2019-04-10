from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

class Department(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department=models.CharField(max_length=100)

@receiver(post_save, sender=User)
def create_user_department(sender, instance, created, **kwargs):
    if created:
        Department.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_department(sender, instance, **kwargs):
    instance.department.save()

class Messege(models.Model):
    title=models.CharField(max_length = 60)
    text=models.TextField()
    # created_time = models.DecimalField()
    name=models.CharField(max_length = 80)

class Post(models.Model):

    department=models.CharField(max_length = 60)
    title=models.CharField(max_length = 60)
    content=RichTextField(max_length = 1000)
    created_date=models.DateTimeField(default = timezone.now)
    published_date=models.DateTimeField(blank = True, null = True)
    author=models.CharField(max_length = 80)

    def __str__(self):
        return self.title
    def __str__(self):
        return self.content
    def approved_comments(self):
        return self.comments.filter(approved_comment = True)


class Comment(models.Model):
    post=models.ForeignKey(
        Post, on_delete = models.CASCADE, related_name = 'comments')
    author=models.CharField(max_length = 200)
    content=models.TextField()
    created_date=models.DateTimeField(default = timezone.now)
    approved_comment=models.BooleanField(default = False)

    def approve(self):
        self.approved_comment=True
        self.save()

    def __str__(self):
        return self.content
