from django.db import models







class CanteenList(models.Model):
    name = models.CharField(max_length=100)
    canteen_id = models.AutoField
    email=models.EmailField(null=True)
    def __str__(self):
        return self.name



class MenuItem(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=100)

    image = models.ImageField(upload_to='menu_images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')
    canteen = models.ForeignKey('CanteenList', null = True, on_delete=models.CASCADE)
    availability = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Availability(models.Model):
    name = models.CharField(max_length=100)

    def  __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class OrderModel(models.Model):

    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField('MenuItem', related_name='order', blank=True)
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)


    is_paid = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'
