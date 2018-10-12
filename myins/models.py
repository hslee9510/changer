from django.db import models
from django.utils import timezone


class Daily(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    type = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return '%s by %s' %(self.title,self.text)
class Todo_Trophy(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    success = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)
    duedate = models.DateField(null=True)
    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Wish(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=True)
    type = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Inspiration(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=True)
    type = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Reference(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=True)
    type = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Trophy(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=True)
    type = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
    def publish(self):
        self.save()

    def __str__(self):
        return self.title
# Create your models here.
'''class Posths(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title'''
