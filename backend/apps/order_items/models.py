from django.db import models # type: ignore
from apps.order.models import Order
from apps.product.models import Product
class Order_Items(models.Model):
    order_item_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20,decimal_places=True)
    
    class Meta:
        db_table = "order_items"