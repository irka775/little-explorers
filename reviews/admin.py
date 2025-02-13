from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'rating','comment', 'created_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('rating', 'created_at')

admin.site.register(Review, ReviewAdmin)
