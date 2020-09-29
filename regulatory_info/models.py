# from django.db import models
# from django.core.validators import MaxValueValidator, MinValueValidator

# # Create your models here.

# halal_status_choices = [
#     ('Contains alcohol', 'Contains alcohol'),
#     ('Inconsistent data', 'Inconsistent data'),
#     ('Halal suitable', 'Halal suitable'),
#     ('Not Halal', 'Not Halal'),
# ]

# class RegulatoryInfo(models.Model):
#     legal_name = models.CharField(max_length=256)
#     alcohol_content = models.FloatField(validators=[ MaxValueValidator(100), MinValueValidator(0)])
#     halal_status = models.CharField(max_length=256, choices=halal_status_choices, default='Halal Suitable')

#     def __str__(self):
#         return self.legal_name
    