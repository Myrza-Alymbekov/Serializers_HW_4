from django.contrib import admin
from django.urls import path
from products import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/category/', views.create_category),
    path('api/category/<int:pk>/', views.detail_category),
    path('api/brand/', views.create_brand),
    path('api/brand/<int:pk>/', views.detail_brand),
    path('api/item/', views.create_item),
    path('api/item/<int:pk>/', views.detail_item),
]

