from django.db import models

# Create your models here.

class User_more(models.Model):
    Name = models.CharField(max_length=30, null=True)
    Surname = models.CharField(max_length=30, null=True)
    Address = models.CharField(max_length=250, null=True)
    Age = models.IntegerField(null=True)
    Company = models.CharField(max_length=250, null=True)
    Status = models.CharField(max_length=250, null=True)
    Creating_Date = models.DateField(null=True)

    def __str__(self):

        return str(self.id) # Display each user id on sqlite page

class Account_more(models.Model):
    Amount = models.IntegerField()
    Creation_Date = models.DateField()
    Account_ID = models.CharField(max_length=30)
    User_ID = models.ForeignKey(User_more, on_delete=models.CASCADE)

    def __str__(self):

        return str(self.id) # Display each account id on sqlite page

