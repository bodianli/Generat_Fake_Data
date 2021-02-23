from django.db import models


# User has identical primary key: 1,2,3...
class User(models.Model):
    fullname = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    age = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)
    # DateField[auto_now=False, auto_now_add=False)
    creatingdate = models.DateField(null=True)

    def __str__(self):
        return str(self.id)


# One user may have many Account, Account is a part of User
class Account(models.Model):
    A_account = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    amount = models.IntegerField(null=True)
    creatingdate = models.DateField(null=True)
    account = models.CharField(max_length=100, null=True)

    # Once i delete User, Account associate with User is delete
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
