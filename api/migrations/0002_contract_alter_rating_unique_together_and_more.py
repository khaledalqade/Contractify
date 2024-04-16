# Generated by Django 4.0.1 on 2024-04-16 05:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_name', models.CharField(blank=True, max_length=255)),
                ('buyer_occupation', models.CharField(blank=True, max_length=255)),
                ('buyer_residence', models.CharField(blank=True, max_length=255)),
                ('buyer_id_type', models.CharField(blank=True, max_length=255)),
                ('buyer_id_number', models.CharField(blank=True, max_length=255)),
                ('buyer_id_expiry_date', models.DateField(blank=True, null=True)),
                ('buyer_id_issuing_authority', models.CharField(blank=True, max_length=255)),
                ('buyer_phone_number', models.CharField(blank=True, max_length=255)),
                ('seller_name', models.CharField(blank=True, max_length=255)),
                ('seller_occupation', models.CharField(blank=True, max_length=255)),
                ('seller_residence', models.CharField(blank=True, max_length=255)),
                ('seller_id_type', models.CharField(blank=True, max_length=255)),
                ('seller_id_number', models.CharField(blank=True, max_length=255)),
                ('seller_id_expiry_date', models.DateField(blank=True, null=True)),
                ('seller_id_issuing_authority', models.CharField(blank=True, max_length=255)),
                ('seller_phone_number', models.CharField(blank=True, max_length=255)),
                ('price_in_digits', models.CharField(blank=True, max_length=255)),
                ('price_in_words', models.CharField(blank=True, max_length=255)),
                ('car_type', models.CharField(blank=True, max_length=255)),
                ('chassis_number', models.CharField(blank=True, max_length=255)),
                ('engine_number', models.CharField(blank=True, max_length=255)),
                ('model', models.CharField(blank=True, max_length=255)),
                ('color', models.CharField(blank=True, max_length=255)),
                ('brand', models.CharField(blank=True, max_length=255)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_update_date', models.DateTimeField(auto_now=True)),
                ('approval', models.BooleanField(default=False)),
                ('buyer_signature', models.BooleanField(default=False)),
                ('seller_signature', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=None,
        ),
        migrations.AlterIndexTogether(
            name='rating',
            index_together=None,
        ),
        migrations.RemoveField(
            model_name='rating',
            name='meal',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.DeleteModel(
            name='Meal',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
