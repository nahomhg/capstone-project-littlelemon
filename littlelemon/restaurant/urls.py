from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = "restaurant"
urlpatterns = [
    path('menu/', views.MenuItemView.as_view(), name="menu_list"),
    path('menu/<int:pk>', views.SingleItemView.as_view(), name="menu_item"),
    path('api-token-auth/',  obtain_auth_token)
]
