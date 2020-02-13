from django.db import models

class Employee(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=100, blank=True, default='')
    address = models.TextField()
    phone_number = models.CharField(max_length=100)
    txId = models.CharField(max_length=100)

    class Meta:
        ordering = ['created']