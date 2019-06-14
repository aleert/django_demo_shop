from django import forms
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.shortcuts import get_object_or_404

from .models import Product, Category
from cart.forms import CartAddProductForm


class ProductListView(ListView):
    """
    Display all products or products in category if <category> passed in url.
    """
    model = Product
    context_object_name = 'products'
    template_name = 'shop/products_in_category.html'

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug', '')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            qs = category.products.filter(available=True).all()
        else:
            qs = super().get_queryset().filter(available=True)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        categories = Category.objects.all()
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        ctx['category'] = self.kwargs.get('category_slug', '')
        ctx['categories'] = categories
        return ctx


class ProductDetailView(FormMixin, DetailView):
    model = Product
    query_pk_and_slug = True
    form_class = CartAddProductForm

    def get_form_kwargs(self):
        product = self.get_object()
        kwargs = super().get_form_kwargs()
        kwargs['max_quantity'] = product.quantity_available
        return kwargs

