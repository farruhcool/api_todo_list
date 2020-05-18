from django.db import models


class Version(models.Model):
    version = models.CharField(max_length=20)

    def __str__(self):
        return self.version


class User(models.Model):
    login = models.CharField(max_length=40)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.login


class ToDo(models.Model):
    user = models.ForeignKey('User', related_name='todos', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title
