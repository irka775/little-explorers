"""
Views for the products application.

This module defines views for displaying, adding, editing, deleting,
and managing products, including wishlist functionality and
 custom error pages.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.http import Http404
from django.urls import reverse

from .models import Product, Category, Wishlist
from .forms import ProductForm


def all_products(request):
    """
    Display all products, including sorting and search functionality.

    This view allows users to filter products by category, search for specific
    products by name or description, and sort them based on selected criteria.
    """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query
            )
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }
    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """
    Display individual product details.

    Raises a 404 error if the product does not exist.
    """
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        print("404 - Product not found")
        raise Http404("Product does not exist")

    context = {
        "product": product,
    }
    return render(request, "products/product_detail.html", context)


def test(request):
    """A test view to render a sample template."""
    return render(request, "products/test.html")


@login_required
def add_product(request):
    """
    Add a new product to the store.

    Only superusers (store owners) are allowed to access this functionality.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to add product. Please ensure the form is valid.",
            )
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {"form": form}
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit an existing product in the store.

    Only superusers (store owners) can perform this action.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to update product. Please ensure the form is valid.",
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "products/edit_product.html"
    context = {"form": form, "product": product}
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store.

    Only superusers (store owners) are allowed to delete products.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products"))


@login_required
def add_to_wishlist(request, product_id):
    """
    Add a product to the user's wishlist.

    If the product is already in the wishlist, a message is displayed.
    """
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)
        wishlist, created = Wishlist.objects.get_or_create(
            customer=request.user
        )

        if product not in wishlist.products.all():
            wishlist.products.add(product)
            messages.success(
                request, f"{product.name} has been added to your wishlist."
            )
        else:
            messages.info(
                request, f"{product.name} is already in your wishlist."
            )

    return redirect("products")  # Redirect back to the products page


@login_required
def remove_from_wishlist(request, product_id):
    """
    Remove a product from the user's wishlist.

    If the wishlist does not exist, an error message is displayed.
    """
    product = get_object_or_404(Product, id=product_id)
    try:
        wishlist = Wishlist.objects.get(customer=request.user)
        if product in wishlist.products.all():
            wishlist.products.remove(product)
            messages.success(
                request,
                f"{product.name} has been removed from your wishlist.",
            )
        else:
            messages.info(
                request, f"{product.name} is not in your wishlist."
            )
    except Wishlist.DoesNotExist:
        messages.error(request, "You don't have a wishlist yet.")

    return redirect("wishlist")  # Redirect back to the wishlist page


@login_required
def wishlist(request):
    """
    Display the user's wishlist.

    If the user does not have a wishlist, an empty response is handled.
    """
    try:
        wishlist = Wishlist.objects.get(customer=request.user)
        wishlist_items = wishlist.products.all()
    except Wishlist.DoesNotExist:
        wishlist_items = (
            None  # Handle the case where no wishlist exists for the user
        )

    return render(
        request, "products/wishlist.html", {"wishlist_items": wishlist_items}
    )


def custom_404(request, exception):
    """Render the custom 404 error page."""
    print("404")
    return render(request, "404.html", status=404)


def custom_500(request):
    """Render the custom 500 error page."""
    print("500")
    return render(request, "500.html", status=500)


def custom_403(request, exception):
    """Render the custom 403 error page."""
    print("403")
    return render(request, "403.html", status=403)


def custom_400(request, exception):
    """Render the custom 400 error page."""
    print("400")
    return render(request, "400.html", status=400)
