"""
Context processor for the shopping bag.

This module provides the `bag_contents` function, which retrieves the 
current shopping bag contents and calculates the order total, 
delivery cost, and applicable discounts.
"""

from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """
    Retrieve shopping bag contents and calculate totals.

    This function extracts product details from the session-based bag,
    calculates the total cost, and determines delivery charges based
    on store settings.

    Args:
        request (HttpRequest): The incoming request.

    Returns:
        dict: A context dictionary containing:
            - `bag_items`: List of items in the bag.
            - `total`: The total cost of items in the bag.
            - `product_count`: The total number of products in the bag.
            - `delivery`: The calculated delivery cost.
            - `free_delivery_delta`: Amount needed to qualify for free delivery.
            - `free_delivery_threshold`: The store's free delivery threshold.
            - `grand_total`: The total cost including delivery charges.
    """
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get("bag", {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)

        if isinstance(
            item_data, int
        ):  # Standard product (no size variation)
            total += item_data * product.price
            product_count += item_data
            bag_items.append(
                {
                    "item_id": item_id,
                    "quantity": item_data,
                    "product": product,
                }
            )
        else:  # Product with size variations
            for size, quantity in item_data["items_by_size"].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append(
                    {
                        "item_id": item_id,
                        "quantity": quantity,
                        "product": product,
                        "size": size,
                    }
                )

    # Calculate delivery charges and free delivery threshold differences
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(
            settings.STANDARD_DELIVERY_PERCENTAGE / 100
        )
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    return {
        "bag_items": bag_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
    }
