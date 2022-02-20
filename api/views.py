from django.shortcuts import render
from django.core import exceptions

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Inventory,Item,Sale
from .serializers import Inventoryserializer,Itemserializer,Saleserializer

class items:

    @api_view(['GET'])
    def get(self):
        items = Item.objects.all()
        serializer = Itemserializer(items,many=True)
        return Response(serializer.data)
    
    @api_view(['POST'])
    def post(self):
        
        serializer = Itemserializer(data=self.data)
        if(serializer.is_valid()):
            serializer.save()
        return Response(serializer.data)
    
    @api_view(['PUT'])
    def update(self,pk):
        item = Item.objects.get(id=pk)
        serializer = Itemserializer(instance=item, data=self.data)
        if(serializer.is_valid()):
            serializer.save()
        
        return Response(serializer.data)
    
    @api_view(['DELETE'])
    def delete(self,pk):
        item = Item.objects.get(id=pk)
        item.delete()
        return Response('deleted!')

class Inventorys:

    @api_view(['GET'])
    def get(self):
        Inventorys = Inventory.objects.all()
        serializer = Inventoryserializer(Inventorys,many=True)
        return Response(serializer.data)
    
    # @api_view(['POST'])
    # def post(self):
        
    #     serializer = Inventoryserializer(data=self.data)
    #     if(serializer.is_valid()):
    #         serializer.save()
    #     return Response(serializer.data)
    
    # @api_view(['PUT'])
    # def update(self,pk):
    #     Inventorys = Inventory.objects.get(id=pk)
    #     serializer = Inventoryserializer(instance=Inventorys, data=self.data)
    #     if(serializer.is_valid()):
    #         serializer.save()
        
    #     return Response(serializer.data)
    
    # @api_view(['DELETE'])
    # def delete(self,pk):
    #     Inventorys = Inventory.objects.get(id=pk)
    #     Inventorys.delete()
    #     return Response('deleted!')


class Sales:

    @api_view(['GET'])
    def get(self):
        Sales = Sale.objects.all()
        serializer = Saleserializer(Sales,many=True)
        return Response(serializer.data)
    
    @api_view(['POST'])
    def post(self):
        
        try:
            items = Item.objects.get(item = self.data['item'])
            Inventorys , created = Inventory.objects.get_or_create(item = items)
            if(created):
                if(self.data['sold_or_buy']=='buy'):
                    serializer = Saleserializer(data=self.data)
                    if(serializer.is_valid()):
                        serializer.save()
                    Inventorys.quantity = self.data['quantity']
                    Inventorys.save()
                    return Response(serializer.data)
                else:
                    return Response(data={"status":404, "error":"Not Found", "message":"No stock"})
            
            else:
                if(self.data['sold_or_buy']=='buy'):
                    serializer = Saleserializer(data=self.data)
                    if(serializer.is_valid()):
                        serializer.save()
                    Inventorys.quantity = Inventorys.quantity + int(self.data['quantity'])
                    Inventorys.save()
                    return Response(serializer.data)
                else:
                    if(Inventorys.quantity - int(self.data['quantity'])>=0):
                        serializer = Saleserializer(data=self.data)
                        if(serializer.is_valid()):
                            serializer.save()
                        Inventorys.quantity = Inventorys.quantity - int(self.data['quantity'])
                        Inventorys.save()
                        return Response(serializer.data)
                    else:
                        return Response(data={"status":404, "error":"Not Found", "message":"No stock"})
        except  exceptions.ObjectDoesNotExist:
            return Response(data={"status":404, "error":"Not Found", "message":"Item Doesn't Exist"})
        
    
    @api_view(['PUT'])
    def update(self,pk):
        Sales = Sale.objects.get(id=pk)

        if(Sales.item.item != self.data['item']):
            Inventorys_2 = Inventory.objects.get(item=self.data['item'])
            Inventorys_1 = Inventory.objects.get(item=Sales.item)
            if(Sales.sold_or_buy=='buy'):
                if(self.data['sold_or_buy']=='buy'):
                    Inventorys_1.quantity = Inventorys_1.quantity - Sales.quantity
                    Inventorys_1.save()
                    Inventorys_2.quantity = Inventorys_2.quantity + int(self.data['quantity'])
                    Inventorys_2.save()
                else:
                    Inventorys_1.quantity = Inventorys_1.quantity - Sales.quantity
                    Inventorys_1.save()
                    Inventorys_2.quantity = Inventorys_2.quantity - int(self.data['quantity'])
                    Inventorys_2.save()
            else:
                if(self.data['sold_or_buy']=='sold'):
                    Inventorys_1.quantity = Inventorys_1.quantity + Sales.quantity
                    Inventorys_1.save()
                    Inventorys_2.quantity = Inventorys_2.quantity + int(self.data['quantity'])
                    Inventorys_2.save()
                else:
                    Inventorys_1.quantity = Inventorys_1.quantity + Sales.quantity
                    Inventorys_1.save()
                    Inventorys_2.quantity = Inventorys_2.quantity + int(self.data['quantity'])
                    Inventorys_2.save()
        
        elif( Sales.item.item==self.data['item'] and (Sales.quantity!=int(self.data['quantity']) or Sales.sold_or_buy!=self.data['sold_or_buy']) ):
            
            Inventorys = Inventory.objects.get(item=self.data['item'])
            if(Sales.sold_or_buy=='buy'):
                if(self.data['sold_or_buy']=='buy'):
                    Inventorys.quantity = Inventorys.quantity - Sales.quantity + int(self.data['quantity'])
                    Inventorys.save()
                else:
                    Inventorys.quantity = Inventorys.quantity - Sales.quantity - int(self.data['quantity'])
                    Inventorys.save()
            else:
                if(self.data['sold_or_buy']=='sold'):
                    Inventorys.quantity = Inventorys.quantity + Sales.quantity - int(self.data['quantity'])
                    Inventorys.save()
                else:
                    Inventorys.quantity = Inventorys.quantity + Sales.quantity + int(self.data['quantity'])
                    Inventorys.save()
        
        Sales.sold_or_buy = self.data['sold_or_buy']
        Sales.save()
        Sales.quantity = int(self.data['quantity'])
        Sales.save()
        Sales.item = Item.objects.get(item=self.data['item'])
        Sales.save() 
        
        serializer = Saleserializer(Sales)

        return Response(serializer.data)
    
    @api_view(['DELETE'])
    def delete(self,pk):
        Sales = Sale.objects.get(id=pk)
        Inventorys = Inventory.objects.get(item=Sales.item)
        if(Sales.sold_or_buy=='buy'):
            Inventorys.quantity = Inventorys.quantity - Sales.quantity
            Inventorys.save()
        else:
            Inventorys.quantity = Inventorys.quantity + Sales.quantity
            Inventorys.save()

        Sales.delete()
        return Response('deleted!')

