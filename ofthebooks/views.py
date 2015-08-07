from django.shortcuts import get_object_or_404, render

from .models import BookReview

# Create your views here.

def index(request, template="index.html", *args, **kwargs):
	reviews = BookReview.objects.all().order_by('-created_date')
	return render(request, template, { "reviews": reviews })

def review(request, slug, template="review.html", *args, **kwargs):
	review = get_object_or_404(BookReview, slug=slug)
	return render(request, template, { "review": review })
