"""
Views for the shopping bag functionality.

This module defines views that handle adding, updating, and removing
products from the shopping bag.
"""

from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404,
)
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """
    Render the shopping bag page.

    Args:
        request (HttpRequest): The incoming request.

    Returns:
        HttpResponse: The rendered shopping bag template.
    """
    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """
    Add a specified quantity of a product to the shopping bag.

    Handles both standard products and those with size variations.

    Args:
        request (HttpRequest): The incoming request.
        item_id (int): The ID of the product to be added.

    Returns:
        HttpResponse: Redirects to the provided redirect URL.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    size = request.POST.get("product_size", None)
    bag = request.session.get("bag", {})

    if size:
        if item_id in bag:
            if size in bag[item_id]["items_by_size"]:
                bag[item_id]["items_by_size"][size] += quantity
                messages.success(
                    request,
                    f'Updated size {size.upper()} {product.name} quantity to'
                    f'{bag[item_id]["items_by_size"][size]}',
                )
            else:
                bag[item_id]["items_by_size"][size] = quantity
                messages.success(
                    request,
                    f"Added size {size.upper()} {product.name} to your bag",
                )
        else:
            bag[item_id] = {"items_by_size": {size: quantity}}
            messages.success(
                request,
                f"Added size {size.upper()} {product.name} to your bag",
            )
    else:
        if item_id in bag:
            bag[item_id] += quantity
            messages.success(
                request, f"Updated {product.name} quantity to {bag[item_id]}"
            )
        else:
            bag[item_id] = quantity
            messages.success(request, f"Added {product.name} to your bag")

    request.session["bag"] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust the quantity of a product in the shopping bag.

    Updates the quantity for standard products and those with sizes.

    Args:
        request (HttpRequest): The incoming request.
        item_id (int): The ID of the product being adjusted.

    Returns:
        HttpResponse: Redirects to the shopping bag page.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    size = request.POST.get("product_size", None)
    bag = request.session.get("bag", {})

    if size:
        if quantity > 0:
            bag[item_id]["items_by_size"][size] = quantity
            messages.success(
                request,
                f'Updated size {size.upper()} {product.name} quantity to'
                f'{bag[item_id]["items_by_size"][size]}',
            )
        else:
            del bag[item_id]["items_by_size"][size]
            if not bag[item_id]["items_by_size"]:
                bag.pop(item_id)
            messages.success(
                request,
                f"Removed size {size.upper()} {product.name} from your bag",
            )
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f"Updated {product.name} quantity to {bag[item_id]}"
            )
        else:
            bag.pop(item_id)
            messages.success(
                request, f"Removed {product.name} from your bag"
            )

    request.session["bag"] = bag
    return redirect(reverse("view_bag"))


def remove_from_bag(request, item_id):
    """
    Remove an item from the shopping bag.

    Handles both standard products and those with size variations.

    Args:
        request (HttpRequest): The incoming request.
        item_id (int): The ID of the product to remove.

    Returns:
        HttpResponse: A 200 response if successful, or 500 if an error occurs.
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = request.POST.get("product_size", None)
        bag = request.session.get("bag", {})

        if size:
            del bag[item_id]["items_by_size"][size]
            if not bag[item_id]["items_by_size"]:
                bag.pop(item_id)
            messages.success(
                request,
                f"Removed size {size.upper()} {product.name} from your bag",
            )
        else:
            bag.pop(item_id)
            messages.success(
                request, f"Removed {product.name} from your bag"
            )

        request.session["bag"] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)
