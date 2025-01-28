from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.



class Review(models.Model):
    customer = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name} by {self.customer.first_name}"

class Wishlist(models.Model):
    customer = models.OneToOneField(User, related_name='wishlist', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='wishlisted_by')

    def __str__(self):
        return f"Wishlist for {self.customer.get_full_name()}"
