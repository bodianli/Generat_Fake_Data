from django.db import models


# User has identical primary key: 1,2,3...
class User(models.Model):
    fullname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    # DateField[auto_now=False, auto_now_add=False)
    creatingdate = models.DateField()

    def __str__(self):
        return str(self.id)


# One user may have many Account, Account is a part of User
class Account(models.Model):
    A_account = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    amount = models.IntegerField()
    creatingdate = models.DateField()
    account = models.CharField(max_length=100)

    # Once i delete User, Account associate with User is delete
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
