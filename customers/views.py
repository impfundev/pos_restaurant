from rest_framework import viewsets, permissions
from customers import serializers
from django.http import HttpResponse


class UserList(viewsets.ModelViewSet):
    queryset = serializers.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CustomerList(viewsets.ModelViewSet):
    queryset = serializers.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


def index(request):
    html = """
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
        </body>
    </html>
    """
    return HttpResponse(html)
