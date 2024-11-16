# Generated by Django 5.0.7 on 2024-08-02 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_usstates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shippers',
            fields=[
                ('shipper_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'shippers',
                'managed': False,
            },
        ),
    ]