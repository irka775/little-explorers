from django.shortcuts import render
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Wishlist
from .forms import ProductForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


from django.http import Http404

def product_detail(request, product_id):
    """ A view to show individual product details """
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        print("404 - Product not found")
        raise Http404("Product does not exist")  # ✅ Asigură-te că returnează un 404 corect

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)


def test(request):
    """ A view to show individual product details """

    return render(request, 'products/test.html')


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_to_wishlist(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)

        # Ensure user has a wishlist
        wishlist, created = Wishlist.objects.get_or_create(
            customer=request.user)

        # Add product to wishlist if not already added
        if product not in wishlist.products.all():
            wishlist.products.add(product)
            messages.success(
                request, f'{product.name} has been added to your wishlist.')
        else:
            messages.info(
                request, f'{product.name} is already in your wishlist.')

    return redirect('products')  # Redirect back to products page


@login_required
def remove_from_wishlist(request, product_id):
    """Remove a product from the wishlist."""
    product = get_object_or_404(Product, id=product_id)
    try:
        # Retrieve the user's wishlist
        wishlist = Wishlist.objects.get(customer=request.user)
        if product in wishlist.products.all():
            wishlist.products.remove(product)  # Remove the product
            messages.success(
                request, f'{product.name} has been removed from your wishlist.')
        else:
            messages.info(request, f'{product.name} is not in your wishlist.')
    except Wishlist.DoesNotExist:
        messages.error(request, "You don't have a wishlist yet.")

    return redirect('wishlist')  # Redirect back to the wishlist page


@login_required
def wishlist(request):
    try:
        wishlist = Wishlist.objects.get(customer=request.user)
        # Retrieve the products in the wishlist
        wishlist_items = wishlist.products.all()
    except Wishlist.DoesNotExist:
        wishlist_items = None  # Handle the case where no wishlist exists for the user

    return render(request, 'products/wishlist.html',
                  {'wishlist_items': wishlist_items})


def custom_404(request, exception):
    print("404")
    return render(request, "404.html", status=404)


def custom_500(request):
    print("500")

    return render(request, "500.html", status=500)


def custom_403(request, exception):
    print("403")

    return render(request, "403.html", status=403)


def custom_400(request, exception):
    print("400")
    return render(request, "400.html", status=400)
