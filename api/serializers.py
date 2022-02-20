from rest_framework import serializers
from .models import Item,Inventory,Sale

class Itemserializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class Inventoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class Saleserializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.sold_or_buy = validated_data.get('sold_or_buy', instance.sold_or_buy)
        instance.item = validated_data.get('item', instance.item)
        instance.save()
        return instance
    
    
    class Meta:
        model = Sale
        fields = '__all__'
