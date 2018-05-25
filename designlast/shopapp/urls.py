from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [

    path('', homepage, name = 'homepage'),
    path('product/<int:id>/', Single_page_views.as_view(), name = 'Single_page_views'),
    path('category/<name>/', Category_View.as_view(), name = 'Category_View'),
    path('shop/', Shop_Project_Views.as_view(), name = 'Shop_Project_Views'),
    path('contact/', Contact_Us_Views, name = 'Contact_Us_Views'),
    path('about-us/', About_us_Views.as_view(), name = 'About_us_Views'),
    path('login/', login_views, name = 'login_views'),
    path('logout/', logout_views, name = 'logout_views'),
    path('dashboard/', dashboard_views, name = 'dashboard_views'),
    path('products/', Products_View.as_view(), name = 'Products_View'),
    path('add-product/', add_prodct_views, name = 'add_prodct_views'),
    path('edit-product/<int:id>/', edit_product_views, name = 'edit_product_views'),
    path('list-item', listOf_product_viwes, name = 'listOf_product_viwes'),
    path('delete-product/<int:id>/', delete_product_viwes, name = 'delete_product_viwes'),
    path('add-slider/', slider_views, name = 'slider_views'),
    path('add-color/', add_Color_Views, name = 'add_Color_Views'),
    path('add-category/', category_views, name = 'category_views'),
    path('add-brand/', adding_brand_views, name = 'adding_brand_views'),
    path('delete-category/<int:id>/', deleteCateogry_Views, name = 'delete_category'),
    path('delete-slider/<int:id>/', deleteSlider_views, name = 'deleteSlider_views'),
    path('update-category/<name>/', update_caategroy, name= 'update_caategroy'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
