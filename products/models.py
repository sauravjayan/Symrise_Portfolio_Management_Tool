from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse_lazy
from datetime import date
from django.utils.text import slugify


physical_form_choices = [
    ('Liquid','Liquid'),
    ('Spray Dried', 'Spray Dried'),
    ('Viscous/Paste', 'Viscous/Paste'),
    ('Wash', 'Wash'),
]

solubility_choices = [
    ('Oil soluble', 'Oil soluble'),
    ('Water soluble', 'Water soluble'),
    ('Water dispersible', 'Water dispersable'),
]

production_site_choices = [
    ('Holzminden', 'Holzminden'),
    ('Noerdlingen', 'Noerdlingen'),
    ('Braunschweig', 'Braunschweig'),
    ('Egypt', 'Egypt'),
]

sales_status_choices = [
    ('FS', 'FS'),
    ('CR', 'CR'),
    ('CC', 'CC'),
    ('CE', 'CE'),
    ('CD', 'CD'),
    ('CT', 'CT'),
]

halal_status_choices = [
    ('Contains alcohol', 'Contains alcohol'),
    ('Inconsistent data', 'Inconsistent data'),
    ('Halal suitable', 'Halal suitable'),
    ('Not Halal', 'Not Halal'),
]

legal_name_choices = [
    ('FLAVOURING', 'FLAVOURING'),
    ('NATURAL FLAVOURING', 'NATURAL FLAVOURING'),
]

# Create your models here.
class Product(models.Model):
    wlc = models.BooleanField('Winning Local Collection',null=True)
    six_digit_code = models.PositiveIntegerField(validators=[ MaxValueValidator(999999), MinValueValidator(100000)], unique=True)
    name = models.CharField(max_length=256)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, editable=False)
    flavour_key = models.CharField(max_length=256)

    # Stock info
    expiry_date = models.DateField(null=True, blank=True)
    order_date = models.DateField(null=True, blank=True)
    arrival_date = models.DateField(null=True, blank=True)
    lab_location = models.CharField(max_length=256, null=True)
    quantity = models.DecimalField(verbose_name='Quantity ( in g )',max_digits=7, decimal_places=3, null=True, validators=[ MinValueValidator(0)])

    # Technical info
    physical_form = models.CharField(choices=physical_form_choices, max_length=256, null=True)
    solubility = models.CharField(choices=solubility_choices, max_length=256, null=True)
    shelf_life = models.PositiveIntegerField(verbose_name='Shelf life ( in days )',null=True)
    storage_condition = models.CharField(max_length=256, null=True)
    production_site = models.CharField(choices=production_site_choices, max_length=256, null=True)

    # Regulatory info
    legal_name = models.CharField(choices=legal_name_choices,max_length=256, null=True)
    alcohol_content = models.FloatField(verbose_name='Alcohol content ( in % )', validators=[ MaxValueValidator(100), MinValueValidator(0)], null=True)
    halal_status = models.CharField(max_length=256, choices=halal_status_choices, default='Halal Suitable', null=True)

    # Additonal info
    sales_status = models.CharField(choices=sales_status_choices, max_length=256, null=True)
    portfolio_manager = models.CharField(max_length=256, null=True)


    def __str__(self):
        return (str(self.six_digit_code) + ' ' + self.name)

    def get_absolute_url(self):
        return reverse_lazy('products:product_detail', kwargs={'slug':self.slug})
    
    def expiry_alert(self):
        if self.expiry_date != None:
            delta = self.expiry_date - date.today()
            return delta.days <= 30
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.six_digit_code)
        super().save(*args, **kwargs)
    
    def is_natural(self):
        return ('natural' in self.legal_name.lower())
            



    