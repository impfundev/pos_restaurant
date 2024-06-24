from django.urls import include, path
from rest_framework import routers
from customers.views import UserList, CustomerList

router = routers.DefaultRouter()
router.register(r"users", UserList)
router.register(r"customers", CustomerList)

urlpatterns = [path("", include(router.urls))]
