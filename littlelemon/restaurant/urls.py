from django.urls import path
from . import views

app_name = "restaurant"
urlpatterns = [
    path('menu', views.MenuItemView.as_view(), name="menu_list"),
    path('menu/<int:pk>', views.SingleItemView.as_view(), name="menu_item"),
]
