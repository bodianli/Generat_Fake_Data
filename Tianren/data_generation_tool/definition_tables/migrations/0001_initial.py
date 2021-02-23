# Generated by Django 2.1.15 on 2020-07-03 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColumnConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('length', models.IntegerField()),
                ('type', models.CharField(choices=[('Integer', 'INT'), ('Character', 'VARCHAR'), ('Decimal', 'DECIMAL'), ('Binary', 'BINARY'), ('Float', 'FLOAT')], default='VARCHAR', max_length=100)),
                ('is_faker_insert', models.BooleanField()),
                ('is_nullable', models.BooleanField()),
                ('is_cascade', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TableConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('schema', models.CharField(max_length=50)),
                ('database_connect', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='columnconfig',
            name='table_config',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='definition_tables.TableConfig'),
        ),
    ]
