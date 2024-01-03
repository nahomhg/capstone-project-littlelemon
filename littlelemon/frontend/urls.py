from django.urls import path, register_converter
from . import views
from django_ratelimit.decorators import ratelimit
from restaurant.date_converter import DateConverter
from restaurant.views import BookingViewSet


app_name="frontend"
register_converter(DateConverter, "date")

urlpatterns = [
    path('menu-items/', ratelimit(key='ip', method='GET', rate='100/min')(views.MenuItemsTemplate.as_view()), name="menu_ui"),
    path('menu-items/<int:pk>', ratelimit(key='ip', method='GET', rate='100/min',) (views.SingeItemTemplateView.as_view()), name="item_detail_ui"),
    path('book/', views.BookTableTemplate.as_view(), name="booking_ui"),
    path('book/<str:booking_date>', BookingViewSet.as_view({'get':'retrieve'}), name="booking_ui_date"),

]
# NOTE: As the frontend of the application requires API calls, we make rate limits so we reduce exposure to and reducing preasure on the server.
