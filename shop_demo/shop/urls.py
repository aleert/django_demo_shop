from django.urls import path

from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.ProductListView.as_view(),
         name='product_list'),
    path('<slug:category_slug>', views.ProductListView.as_view(),
         name='products_in_category'),
    path('<int:pk>/<slug:slug>/', views.ProductDetailView.as_view(),
         name='product_detail')
]
