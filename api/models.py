from django.db import models

class Item(models.Model):
    item = models.CharField(max_length=100,unique=True)

    def __str__(self) -> str:
        return self.item

class Inventory(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE,to_field='item')
    quantity = models.IntegerField(default=0)
    describe = models.CharField(max_length=100,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.item.item

class Sale(models.Model):

    MY_CHOICES = (
        ('sold', 'sold'),
        ('buy', 'buy'),
    )

    item = models.ForeignKey(Item,on_delete=models.CASCADE,to_field='item')
    quantity = models.IntegerField()
    describe = models.CharField(max_length=100,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    sold_or_buy = models.CharField(max_length=50, choices=MY_CHOICES)

    def __str__(self) -> str:
        return self.item.item

