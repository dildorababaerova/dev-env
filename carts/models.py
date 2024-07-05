from goods.models import Product
from django.db import models

from users.models import User


class CartQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Käyttäjä')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Tuote')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Määrä')
    session_key= models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Lisätty aika')
    
    class Meta:
        db_table = 'cart'
        verbose_name = 'kori'
        verbose_name_plural = 'korit'

    objects = CartQueryset.as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)
        
    def __str__(self):
        return f'Kori {self.user.username} | Tuote {self.product.name} | Määrä {self.quantity} | Lisätty aika {self.created_timestamp}' 
