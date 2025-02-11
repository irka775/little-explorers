from django.db import models
from django.contrib.auth.models import User
from products.models import Product  # Asigură-te că ai aplicația 'products' în INSTALLED_APPS

class Review(models.Model):
    REVIEW_TYPE_CHOICES = [
        ('product', 'Product Review'),
        ('site', 'Site Feedback'),
    ]
    
    customer = models.ForeignKey(
        User, related_name='reviews', on_delete=models.CASCADE
    )
    review_type = models.CharField(
        max_length=10, choices=REVIEW_TYPE_CHOICES, default='product'
    )
    product = models.ForeignKey(
        Product, related_name='reviews', on_delete=models.CASCADE, 
        blank=True, null=True
    )
    rating = models.PositiveIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)], blank=True, null=True
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.review_type == 'product' and self.product:
            return f"Review for {self.product.name} by {self.customer.username}"
        return f"Site Feedback by {self.customer.username}"
