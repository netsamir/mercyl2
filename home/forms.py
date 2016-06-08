from django import forms

from .models import (Customer, Machine, Transport, TaxCountry, CustomUruguay,
        TasaServicioAduana, ExtraordinarioPrice, PortPrice, CustomBrokerPrice)

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['email', 'phone', 'fullname', 'purchase', 'contacted',
                'city', 'country']

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['name', 'purchase_price', 'sale_price', 'sold_price',
                'weight', 'length', 'width']

class TransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ['base_price']

class TaxCountryForm(forms.ModelForm):
    class Meta:
        model = TaxCountry
        fields = ['country', 'tax']

class CustomUruguayForm(forms.ModelForm):
    class Meta:
        model = CustomUruguay
        fields = ['country', 'recargo', 'imudani', 'tsa', 'extraordinario',
                'guia', 'tasa', 'anticipo_irae', 'anticipo_imesi', 'puerto',
                'iva', 'anticipo_iva', 'gastos_y_otros', 'flete_local',
                'playa_de_contenedores']

class TasaServicioAduanaForm(forms.ModelForm):
    class Meta:
        model = TasaServicioAduana
        fields = ['valor_cif_inf', 'valor_cif_sup', 'percentage']

class ExtraordinarioPriceForm(forms.ModelForm):
    class Meta:
        model = ExtraordinarioPrice
        fields = ['valor_cif_inf', 'valor_cif_sup', 'percentage']

class PortPriceForm(forms.ModelForm):
    class Meta:
        model = PortPrice
        fields = ['ton_inf', 'ton_sup', 'percentage']

class CustomBrokerPriceForm(forms.ModelForm):
    class Meta:
        model = CustomBrokerPrice
        fields = ['valor_cif_inf', 'valor_cif_sup', 'percentage']
