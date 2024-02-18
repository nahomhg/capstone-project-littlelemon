from django.urls import path, include
from restaurant import views as api_views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()

# router.register(r'booking', viewset=api_views.BookingViewSet, basename="make_booking");

app_name = "restaurant"
urlpatterns = [
    path('menu/', api_views.MenuItemView.as_view()),
    path('menu/<int:pk>', api_views.SingleItemView.as_view()),
    path('', include(router.urls)),
    path('create', api_views.BookingCreate.as_view(), name="create"),
    path('bookings/<str:booking_date>', api_views.BookingCreate.as_view(), name="booking_list"),
    path('bookings/<str:booking_date>/<str:booking_slot>', api_views.BookingDetail.as_view(), name="booking_list_detail"),
    path('api-token-auth/',  obtain_auth_token),
]

 # path('booking/<str:booking_date>/<int:booking_slot>/', api_views.BookingViewSet.as_view({'get':'booking_detail'}), name="detail_booking"),
    # path('booking/<str:booking_date>', api_views.BookingViewSet.as_view({'get':'retrieve'}), name="list_booking"),
    # # path('booking/<int:pk>', api_views.BookingViewSet(), name="update_booking"),