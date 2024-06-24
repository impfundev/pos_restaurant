from rest_framework import viewsets, permissions
from customers import serializers


class UserList(viewsets.ModelViewSet):
    queryset = serializers.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CustomerList(viewsets.ModelViewSet):
    queryset = serializers.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
