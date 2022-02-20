from django.urls import path

from .views import items,Inventorys,Sales

urlpatterns = [
    #items
    path('item/get', items.get,name="itemget"),
    path("item/post",items.post,name="itempost"),
    path("item/update/<int:pk>",items.update,name="itemupdate"),
    path("item/delete/<int:pk>",items.delete,name="itemdelete"),

    #inventory
    path('inventory/get', Inventorys.get,name="Inventoryget"),
    # path("inventory/post",Inventorys.post,name="Inventorypost"),
    # path("inventory/update",Inventorys.update,name="Inventoryupdate"),
    # path("inventory/detele",Inventorys.delete,name="Inventorydelete"),

    #sale
    path('sale/get', Sales.get,name="Saleget"),
    path("sale/post",Sales.post,name="Salepost"),
    path("sale/update/<int:pk>",Sales.update,name="Saleupdate"),
    path("sale/delete/<int:pk>",Sales.delete,name="Saledelete"),

]
