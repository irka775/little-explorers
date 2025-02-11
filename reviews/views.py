from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from .forms import ReviewForm

# 1️⃣ Listă de recenzii
def review_list(request):
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

# 2️⃣ Creare recenzie/feedback
@login_required
def review_create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.customer = request.user
            form.save()
            messages.success(request, "Review submitted successfully!")
            return redirect('review_list')
    else:
        form = ReviewForm()
    
    return render(request, 'reviews/review_form.html', {'form': form})

# 3️⃣ Editare recenzie
@login_required
def review_edit(request, review_id):
    review = get_object_or_404(Review, id=review_id, customer=request.user)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated successfully!")
            return redirect('review_list')
    else:
        form = ReviewForm(instance=review)
    
    return render(request, 'reviews/review_form.html', {'form': form})

# 4️⃣ Ștergere recenzie
@login_required
def review_delete(request, review_id):
    review = get_object_or_404(Review, id=review_id, customer=request.user)
    if request.method == "POST":
        review.delete()
        messages.success(request, "Review deleted successfully!")
        return redirect('review_list')
    
    return render(request, 'reviews/review_confirm_delete.html', {'review': review})
