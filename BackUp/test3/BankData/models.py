from django.db import models

# User has identical primary key: 1,2,3...
class User(models.Model):
    FullName = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    Age = models.CharField(max_length=100)
    Company = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)
    # DateField[auto_now=False, auto_now_add=False)
    Creating_Date = models.DateField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):

        return str(self.id)

# One user may have many Account, Account is a part of User
class Account(models.Model):
    Amount = models.IntegerField()
    Creating_Date = models.DateField()
    # Once i delete User, Account associate with User is delete
    number = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return str(self.id)

    '''
    # Method 1. Create a calss to insert data
    @classmethod
    def createAccount(cls, AAmount, ACreating_Date, Anumber):
        record = cls(Amount=AAmount, Creating_Date=ACreating_Date, number=Anumber)
        return record
    '''