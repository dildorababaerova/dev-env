from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Kategoria')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategoriat'

    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=150, verbose_name='Nimi')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description=models.TextField(blank=True, null=True, verbose_name='Kuvaus')
    price=models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Hinta')
    discount_price=models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Alennettu hinta')    
    image=models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Kuva')
    quantity=models.IntegerField(default=0, verbose_name='Määrä')
    category=models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='Kategoria')


    class Meta:
        verbose_name = 'Tuote'
        verbose_name_plural = 'Tuotteet'
        ordering = ("id",) 

    def __str__(self):
        return f'{self.name} Määrä - {self.quantity} Hinta - {self.price}'
    
    def display_id(self):
        return f'{25225+self.id:05}' 

    def sell_price(self):
        if self.discount_price:
            return round(self.price-self.price*self.discount_price/100, 2)
        return self.price 