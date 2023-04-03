from django.contrib import admin
from django.urls import path,include

from rest_framework import routers
from users.api.viewsets import UserViewSet, GeneralAccountViewSet, BalanceViewSet, PurchaseViewSet
from users.views import UserCreateView, UserList, UserDetailView, UserUpdateView
route = routers.DefaultRouter()

route.register(r'users', UserViewSet, basename='Users')
route.register(r'generalAccount', GeneralAccountViewSet, basename='GeneralAccount')
route.register(r'balance', BalanceViewSet, basename='Balances')
route.register(r'purchase', PurchaseViewSet, basename='Purchases')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('createUser/', UserCreateView.as_view(), name='user_create'),
    path('listUser/', UserList.as_view(), name='user_list'),
    path('deleteUser/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('updateUser/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('', include(route.urls)),
]

