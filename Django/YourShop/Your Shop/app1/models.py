from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


"""
    This file lists all the models used in the project.
    The models are the tables in the database, where the entries are the columns and each entry corresponds to a row
"""


class category(models.Model): # to specify the category of an item
    name=models.CharField(max_length=200)
    def get_absolute_url(self):
        return reverse('app1:detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.name

    def get_item(self):
        return item.objects.filter(category=self)

class item(models.Model):  #the item model for the items
    cat=models.ForeignKey(category, on_delete=models.CASCADE) # foreign key specifies the category of the product
    name=models.CharField(max_length=250)
    product_id=models.IntegerField(unique=True)
    price=models.FloatField()
    rating=models.FloatField(default=None)
    in_cart=models.BooleanField(default=False)
    pic=models.FileField(default=None)    #file field to display the picture of the item

    def get_absolute_url(self):
        return reverse('app1:detail', kwargs={'pk': self.product_id})
    def __str__(self):
        return self.name + ' - ' + self.cat.name


class item_review(models.Model):
    product=models.ForeignKey(item, on_delete=models.CASCADE)
    comment=models.CharField(max_length=512)

    def get_absolute_url(self):
        return reverse('app1:detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.name + ' - ' + self.cat.name

class delivery(models.Model):
    name=models.CharField(max_length=150)
    house_no=models.CharField(max_length=20)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode=models.CharField(max_length=8)

