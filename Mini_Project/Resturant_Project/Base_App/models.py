from django.db import models

# Create your models here.
class ItemList(models.Model):
    Category_name = models.CharField(max_length=15)

    def __str__(self):
        return self.Category_name
    

class Items(models.Model):
    Item_name = models.CharField(max_length=40)
    description = models.TextField(blank=False)
    Price = models.IntegerField()
    Category = models.ForeignKey(ItemList, related_name='Name', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.Item_name

class Order(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField(default=1)
    customer_name = models.CharField(max_length=100, default="Anonymous")
    contact_number = models.CharField(max_length=15, default="0000000000")
    address = models.TextField(default="Not provided")
    pincode = models.CharField(max_length=10, default="000000")
    created_at = models.DateTimeField(default="2024-01-01 00:00:00")


    def __str__(self):
        return f"Order for {self.item.Item_name} (x{self.quantity})"


class AboutUs(models.Model):
    Description = models.TextField(blank=False)

class Feedback(models.Model):
    Name = models.CharField(max_length=100, default="Anonymous")
    Description = models.TextField()
    Rating = models.IntegerField()
    Image = models.ImageField(upload_to='feedback_images/', blank=True, null=True)


    def __str__(self):
        return self.Name
    

class BookTable(models.Model):
    Name = models.CharField(max_length=15)
    Phone_number = models.IntegerField()
    Email = models.EmailField()
    Total_person = models.IntegerField()
    Booking_date = models.DateField()

    def __str__(self):
        return self.Name