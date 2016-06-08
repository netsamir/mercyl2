from django.contrib import admin

# Register your models here.
from .models import (Customer, Machine, Transport, TaxCountry, CustomUruguay,
        TasaServicioAduana, ExtraordinarioPrice, PortPrice, CustomBrokerPrice)

from .forms import (CustomerForm, MachineForm, TransportForm,
        TaxCountryForm, CustomUruguayForm, TasaServicioAduanaForm,
        ExtraordinarioPriceForm, PortPriceForm, CustomBrokerPriceForm)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'city']
    form = CustomerForm

class MachineAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    form = MachineForm

class TransportAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    form = TransportForm

class TaxCountryAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    form = TaxCountryForm

class CustomUruguayAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    form = CustomUruguayForm

class TasaServicioAduanaAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    form = TasaServicioAduanaForm

class ExtraordinarioPriceAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    form = ExtraordinarioPriceForm

class PortPriceAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    form = PortPriceForm

class CustomBrokerPriceAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    form = CustomBrokerPriceForm

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Machine, MachineAdmin)
admin.site.register(Transport, TransportAdmin)
admin.site.register(TaxCountry, TaxCountryAdmin)
admin.site.register(CustomUruguay, CustomUruguayAdmin)
admin.site.register(TasaServicioAduana, TasaServicioAduanaAdmin)
admin.site.register(ExtraordinarioPrice, ExtraordinarioPriceAdmin)
admin.site.register(PortPrice, PortPriceAdmin)
admin.site.register(CustomBrokerPrice, CustomBrokerPriceAdmin)

