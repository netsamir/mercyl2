from django.db import models


COUNTRY = (
    ('UYU', 'Uruguay'),
    ('ARG', 'Argentina'),
    ('BRA', 'Brazil'),
    ('PRY', 'Parguay')
)


# Create your models here.
class Customer(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=120)
    fullname = models.CharField(max_length=120)
    purchase = models.DecimalField(max_digits=7, decimal_places=0)
    contacted = models.BooleanField()
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=3, choices=COUNTRY)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email

class Machine(models.Model):
    """Every machine has some features"""
    name = models.CharField(max_length=120)
    purchase_price = models.DecimalField(max_digits=7, decimal_places=0)
    sale_price = models.DecimalField(max_digits=7, decimal_places=0)
    sold_price = models.DecimalField(max_digits=7, decimal_places=0)
    weight = models.DecimalField(max_digits=7, decimal_places=0)
    length = models.DecimalField(max_digits=7, decimal_places=0)
    width = models.DecimalField(max_digits=7, decimal_places=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

class Transport(models.Model):
    base_price = models.DecimalField(max_digits=7, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

class TaxCountry(models.Model):
    country = models.CharField(max_length=120)
    tax = models.DecimalField(max_digits=7, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

class CustomUruguay(models.Model):
    country = models.CharField(max_length=120)
    recargo = models.DecimalField(max_digits=7, decimal_places=2)
    imudani = models.DecimalField(max_digits=7, decimal_places=2)
    tsa = models.DecimalField(max_digits=7, decimal_places=2)
    extraordinario = models.DecimalField(max_digits=7, decimal_places=2)
    guia = models.DecimalField(max_digits=7, decimal_places=2)
    tasa = models.DecimalField(max_digits=7, decimal_places=2)
    anticipo_irae = models.DecimalField(max_digits=7, decimal_places=2)
    anticipo_imesi = models.DecimalField(max_digits=7, decimal_places=2)
    puerto = models.DecimalField(max_digits=7, decimal_places=2)
    iva = models.DecimalField(max_digits=7, decimal_places=2)
    anticipo_iva = models.DecimalField(max_digits=7, decimal_places=2)
    gastos_y_otros = models.DecimalField(max_digits=7, decimal_places=2)
    flete_local = models.DecimalField(max_digits=7, decimal_places=2)
    playa_de_contenedores = models.DecimalField(max_digits=7, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.country

class TasaServicioAduana(models.Model):
    valor_cif_inf = models.DecimalField(max_digits=7, decimal_places=2)
    valor_cif_sup = models.DecimalField(max_digits=7, decimal_places=2)
    percentage = models.DecimalField(max_digits=7, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.percentage

class ExtraordinarioPrice(models.Model):
    valor_cif_inf = models.DecimalField(max_digits=7, decimal_places=2)
    valor_cif_sup = models.DecimalField(max_digits=7, decimal_places=2)
    percentage = models.DecimalField(max_digits=7, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.percentage

class PortPrice(models.Model):
    ton_inf = models.DecimalField(max_digits=7, decimal_places=2)
    ton_sup = models.DecimalField(max_digits=7, decimal_places=2)
    percentage = models.DecimalField(max_digits=7, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.percentage

class CustomBrokerPrice(models.Model):
    valor_cif_inf = models.DecimalField(max_digits=7, decimal_places=2)
    valor_cif_sup = models.DecimalField(max_digits=7, decimal_places=2)
    percentage = models.DecimalField(max_digits=7, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.percentage
# Create your models here.
