from django.db import models # type: ignore
from apps.clients.models import Customer
class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=20,decimal_places=True)
    
    class Meta:
        db_table = "order"
        

