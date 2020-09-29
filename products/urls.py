from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('home/', views.ProductTemplateView.as_view(), name='home'),
    path('product_detail/<slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('natural_product_list/', views.NaturalProductListView.as_view(), name='products_list'),
    path('natural_identical_product_list/', views.NaturalIdenticalProductListView.as_view(), name='ni_products_list'),
    path('create/', views.ProductCreateView.as_view(), name='create'),
    path('search_list/<name>/', views.ProductSearchListView.as_view(), name='search_list'),
    path('ni_search_list/<name>/', views.NIProductSearchListView.as_view(), name='ni_search_list'),
    path('uni_search_list/<name>/', views.UniversalSearchListView.as_view(), name='uni_search_list'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='update'),
    path('quantity_update/<slug>/', views.QuantityUpdateView.as_view(), name='quantity_update'),
    path('filter_products/', views.filter, name='filter'),
    path('filter_list/<flavour_key>/<alcohol_content>/<production_site>/<solubility>/', views.FilterListView.as_view(), name='filter_list'),
    path('ni_filter_products/', views.ni_filter, name='ni_filter'),
    path('ni_filter_list/<flavour_key>/<alcohol_content>/<production_site>/<solubility>/', views.NIFilterListView.as_view(), name='ni_filter_list'),
    path('export/<qset>/', views.export_to_xlsx, name='export'),
]