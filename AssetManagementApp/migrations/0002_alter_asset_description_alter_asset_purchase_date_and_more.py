# Generated by Django 4.0.3 on 2024-01-08 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetManagementApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='purchase_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='assetcategory',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='assetcategory',
            name='is_laptop',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='is_cisco_product',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='is_cloudops_product',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='is_splunk_product',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='permission',
            name='value',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='is_default_for_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='status',
            name='show_on_dashboard_code',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
