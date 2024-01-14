from django.urls import path, register_converter
from . import views as frontend_views
from django_ratelimit.decorators import ratelimit
from restaurant.date_converter import DateConverter
from restaurant import views as api_views


app_name="frontend"
register_converter(DateConverter, "date")

urlpatterns = [
    path('menu-items/', frontend_views.MenuItemsTemplate.as_view(), name="menu_ui"),
    path('menu-items/<int:pk>', frontend_views.SingeItemTemplateView.as_view(), name="item_detail_ui"),
    path('book/', frontend_views.BookTableTemplate.as_view(), name="booking_ui"),
    path('book/<str:booking_date>', api_views.BookingViewSet.as_view({'get':'list'}), name="booking_ui_date"),

]
# NOTE: As the frontend of the application requires API calls, we make rate limits so we reduce exposure to and reducing preasure on the server.
