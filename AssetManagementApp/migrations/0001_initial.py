# Generated by Django 4.2.3 on 2023-12-18 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetCategory',
            fields=[
                ('asset_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('is_laptop', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('laptop_id', models.AutoField(primary_key=True, serialize=False)),
                ('asset_id', models.IntegerField()),
                ('wifi_mac_address', models.CharField(max_length=50)),
                ('lan_mac_address', models.CharField(max_length=50)),
                ('os', models.CharField(max_length=50)),
                ('processor', models.CharField(max_length=50)),
                ('ram', models.CharField(max_length=50)),
                ('disk_type', models.CharField(max_length=50)),
                ('disk_capacity', models.CharField(max_length=50)),
                ('is_cisco_product', models.BooleanField()),
                ('is_cloudops_product', models.BooleanField()),
                ('is_splunk_product', models.BooleanField()),
                ('splunk_id', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('color_code', models.CharField(max_length=50)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('show_on_dashboard_code', models.BooleanField()),
                ('is_default_for_status', models.BooleanField()),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.CharField(max_length=50)),
                ('mobile_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('mobile_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AssetManagementApp.location')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('permission_id', models.AutoField(primary_key=True, serialize=False)),
                ('module', models.CharField(max_length=100)),
                ('value', models.BooleanField()),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AssetManagementApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('asset_id', models.AutoField(primary_key=True, serialize=False)),
                ('asset_code', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=100)),
                ('serial_number', models.IntegerField()),
                ('purchase_date', models.DateField(blank=True, null=True)),
                ('purchase_cost', models.IntegerField(blank=True, null=True)),
                ('warranty', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('asset_category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AssetManagementApp.assetcategory')),
                ('employee_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AssetManagementApp.user')),
                ('room_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AssetManagementApp.room')),
                ('status_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AssetManagementApp.status')),
                ('supplier_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AssetManagementApp.supplier')),
            ],
        ),
    ]