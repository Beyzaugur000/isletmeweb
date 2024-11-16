# Generated by Django 5.0.7 on 2024-08-02 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_customers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_id', models.IntegerField(blank=True, null=True)),
                ('order_date', models.DateTimeField(blank=True, null=True)),
                ('required_date', models.DateTimeField(blank=True, null=True)),
                ('shipped_date', models.DateTimeField(blank=True, null=True)),
                ('ship_via', models.IntegerField(blank=True, null=True)),
                ('freight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ship_name', models.CharField(blank=True, max_length=255, null=True)),
                ('ship_address', models.CharField(blank=True, max_length=255, null=True)),
                ('ship_city', models.CharField(blank=True, max_length=100, null=True)),
                ('ship_region', models.CharField(blank=True, max_length=100, null=True)),
                ('ship_postal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('ship_country', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
    ]
