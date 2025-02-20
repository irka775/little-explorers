"""
Django views for managing product reviews.

This module includes:
- `review_list`: Displays all reviews.
- `review_create`: Allows logged-in users to submit reviews.
- `review_edit`: Allows users to update their own reviews.
- `review_delete`: Allows users to delete their own reviews.

All views use Django messages to provide user feedback.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from .forms import ReviewForm


def review_list(request):
    """
    Displays a list of all submitted reviews.

    Retrieves all reviews from the database, ordered by their creation date
    (newest first), and renders them in the `review_list.html` template.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Renders the review list template.
    """
    reviews = Review.objects.all().order_by("-created_at")
    return render(request, "reviews/review_list.html", {"reviews": reviews})


@login_required
def review_create(request):
    """
    Handles the creation of a new review.

    Only logged-in users can submit a review. If the request is a POST request,
    it validates the form and saves the review, associating it with the
    currently logged-in user.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Redirects to the review list upon successful submission.
    """
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.customer = (
                request.user
            )  # Assigns the logged-in user as the author
            review.save()
            messages.success(request, "Review submitted successfully!")
            return redirect("review_list")
    else:
        form = ReviewForm()

    return render(request, "reviews/review_form.html", {"form": form})


@login_required
def review_edit(request, review_id):
    """
    Allows a logged-in user to edit their own review.

    The function ensures that the user can only edit their own reviews. If
    the form is submitted successfully, the updated review is saved.

    Args:
        request (HttpRequest): The request object.
        review_id (int): The ID of the review being edited.

    Returns:
        HttpResponse: Redirects to the review list upon successful update.
    """
    review = get_object_or_404(Review, id=review_id, customer=request.user)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated successfully!")
            return redirect("review_list")
    else:
        form = ReviewForm(instance=review)

    return render(request, "reviews/review_form.html", {"form": form})


@login_required
def review_delete(request, review_id):
    """
    Allows a logged-in user to delete their own review.

    Users can only delete reviews they have written. A confirmation page is
    displayed before deletion.

    Args:
        request (HttpRequest): The request object.
        review_id (int): The ID of the review being deleted.

    Returns:
        HttpResponse: Redirects to the review list upon successful deletion.
    """
    review = get_object_or_404(Review, id=review_id, customer=request.user)
    if request.method == "POST":
        review.delete()
        messages.success(request, "Review deleted successfully!")
        return redirect("review_list")

    return render(
        request, "reviews/review_confirm_delete.html", {"review": review}
    )
