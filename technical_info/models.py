# from django.db import models

# # Create your models here.

# physical_form_choices = [
#     ('Liquid','Liquid'),
#     ('Spray Dried', 'Spray Dried'),
#     ('Viscous/Paste', 'Viscous/Paste'),
#     ('Wash', 'Wash'),
# ]

# solubility_choices = [
#     ('Oil soluble', 'Oil soluble'),
#     ('Water soluble', 'Water soluble'),
#     ('Water dispersible', 'Water dispersable'),
# ]

# production_site_choices = [
#     ('Holzminden', 'Holzminden'),
#     ('Noerdlingen', 'Noerdlingen'),
#     ('Braunschweig', 'Braunschweig'),
#     ('Egypt', 'Egypt'),
# ]

# class TechnicalInfo(models.Model):
#     physical_form = models.CharField(choices=physical_form_choices, max_length=256)
#     solubility = models.CharField(choices=solubility_choices, max_length=256)
#     shelf_life = models.PositiveIntegerField()
#     storage_condition = models.CharField(max_length=256)
#     production_site = models.CharField(choices=production_site_choices, max_length=256)

#     def __str__(self):
#         return f'Shelf Life: {self.shelf_life} days'

