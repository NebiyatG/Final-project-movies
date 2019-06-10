from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MovieType(models.Model):
    movietypename=models.CharField(max_length='255')
    moviedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.movietypename

    class Meta:
        db_table='movietype'
        verbose_name_pliral='muvietypes'

    class product(models.model):
        productname=models.CharField(max_length='255')
        movietype =models.ForeignKey(MuvieType, on_delet=models.Cascade.DO_NOTHING)
        user=models.ForeignKey(Userm on_delete=models.DO_NOTHING)
        Productprice=models.DecimalField(max_digits=10, decimal_places=2)
        productentydate=models.DateField()
        productURL=models.URLField(null=True, blank=True)
        productdescription=models.textField(null=True, blank=True)

        def __str__(self): 
            return self.productname

        def memberDiscount(self):
            discount=.05
            returnfloat(self.productprice) * discount

        def discointedPrice(self):
            discount=self.memberDiscuint()
            return float(self.productprice)-discount

        class Meta:
            db_table='product'
            verbose_name_plural='products'


