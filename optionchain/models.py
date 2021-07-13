from django.db import models

# Create your models here.

class Underlying(models.Model):
    name = models.CharField(max_length=256, null=True)
    type = models.CharField(max_length=256, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Openinterest(models.Model):
    timestamp = models.CharField(max_length=256, null=True)
    strikeType = models.CharField(max_length=256, null=True)
    strikePrice = models.IntegerField(null=True)
    expiryDate = models.CharField(max_length=256, null=True)
    identifier = models.CharField(max_length=256, null=True)
    openInterest = models.IntegerField(null=True)
    changeinOpenInterest = models.IntegerField(null=True)
    pchangeinOpenInterest = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    totalTradedVolume = models.IntegerField(null=True)
    impliedVolatility = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    lastPrice = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    change = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    pChange = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    totalBuyQuantity = models.IntegerField(null=True)
    totalSellQuantity = models.IntegerField(null=True)
    bidQty = models.IntegerField(null=True)
    bidprice = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    askQty = models.IntegerField(null=True)
    askPrice = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    underlyingValue = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    underlying = models.ForeignKey(Underlying, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Totalinterest(models.Model):
    underlying = models.ForeignKey(Underlying, on_delete=models.CASCADE)
    ce_totoi = models.IntegerField(null=True)
    ce_totvol = models.IntegerField(null=True)
    pe_totoi = models.IntegerField(null=True)
    pe_totvol = models.IntegerField(null=True)
    timestamp = models.CharField(max_length=256, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)