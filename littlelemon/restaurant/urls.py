from django.urls import path, include
from . import views

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'', viewset=views.BookingViewSet);

app_name = "restaurant"
urlpatterns = [
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleItemView.as_view()),
    path('booking/', include(router.urls)),
    path('booking/<str:date>', include(router.urls)),
    path('api-token-auth/',  obtain_auth_token),
]
