from django.contrib import admin
from django.urls import path, include

from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Blog API')  # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('schema/', schema_view),
]
