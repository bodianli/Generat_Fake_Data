from django.db import models


# Table has identical primary key: 1,2,3...
class TableConfig(models.Model):
    name = models.CharField(max_length=50)
    schema = models.CharField(max_length=50)
    database_connect = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


# One table may have many columns, column is a part of table
class ColumnConfig(models.Model):
    INT = 'Integer'
    VARCHAR = 'Character'
    DECIMAL = 'Decimal'
    BINARY = 'Binary'
    FLOAT = 'Float'
    DATA_TYPE_CHOICES = [
        (INT, 'INT'),
        (VARCHAR, 'VARCHAR'),
        (DECIMAL, 'DECIMAL'),
        (BINARY, 'BINARY'),
        (FLOAT, 'FLOAT')
    ]
    name = models.CharField(max_length=100)
    length = models.IntegerField()
    type = models.CharField(
        max_length=100,
        choices=DATA_TYPE_CHOICES,
        default='VARCHAR'
    )
    is_faker_insert = models.BooleanField()
    is_nullable = models.BooleanField()
    is_cascade = models.BooleanField()
    table_config = models.ForeignKey(TableConfig, on_delete=models.CASCADE)

    # Once delete Table, column associate with Table is delete
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + ' ' + str(self.table_config)
