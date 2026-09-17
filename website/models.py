from django.db import models


class Contact (models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    massage = models.CharField()
    update_date = models.DateTimeField (auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta :
        ordering = ["created_date"]

    def __str__(self):
        return self.name