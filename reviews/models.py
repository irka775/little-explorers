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
