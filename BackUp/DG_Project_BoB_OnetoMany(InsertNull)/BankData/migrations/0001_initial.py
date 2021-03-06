# Generated by Django 2.1.15 on 2020-06-16 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=100)),
                ('creatingdate', models.CharField(max_length=100)),
                ('account', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('creatingdate', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='A_account',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='BankData.User'),
        ),
    ]
