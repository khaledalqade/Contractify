
from django.db import models
from django.utils import timezone


class Contract(models.Model):
    buyer_name = models.CharField(max_length=255, blank=True)
    buyer_occupation = models.CharField(max_length=255, blank=True)
    buyer_residence = models.CharField(max_length=255, blank=True)
    buyer_id_type = models.CharField(max_length=255, blank=True)
    buyer_id_number = models.CharField(max_length=255, blank=True)
    buyer_id_expiry_date = models.DateField(blank=True, null=True)
    buyer_id_issuing_authority = models.CharField(max_length=255, blank=True)
    buyer_phone_number = models.CharField(max_length=255, blank=True)
    seller_name = models.CharField(max_length=255, blank=True)
    seller_occupation = models.CharField(max_length=255, blank=True)
    seller_residence = models.CharField(max_length=255, blank=True)
    seller_id_type = models.CharField(max_length=255, blank=True)
    seller_id_number = models.CharField(max_length=255, blank=True)
    seller_id_expiry_date = models.DateField(blank=True, null=True)
    seller_id_issuing_authority = models.CharField(max_length=255, blank=True)
    seller_phone_number = models.CharField(max_length=255, blank=True)
    price_in_digits = models.CharField(max_length=255, blank=True)
    price_in_words = models.CharField(max_length=255, blank=True)
    car_type = models.CharField(max_length=255, blank=True)
    chassis_number = models.CharField(max_length=255, blank=True)
    engine_number = models.CharField(max_length=255, blank=True)
    model = models.CharField(max_length=255, blank=True)
    color = models.CharField(max_length=255, blank=True)
    brand = models.CharField(max_length=255, blank=True)
    creation_date = models.DateTimeField(default=timezone.now)
    last_update_date = models.DateTimeField(auto_now=True)
    approval = models.BooleanField(default=False)
    buyer_signature = models.BooleanField(default=False)
    seller_signature = models.BooleanField(default=False)
