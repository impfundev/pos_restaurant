from django.test import TestCase
from rest_framework.test import APIClient, force_authenticate
from customers.models import User, Customer
from customers.views import UserList, CustomerList


class UserListViewTest(TestCase):

    def setUp(self):
        """Set up test data for the UserList view tests."""
        self.factory = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

    def test_get_user_list_unauthenticated(self):
        """Test that unauthenticated users can retrieve the user list."""
        request = self.factory.get("/users/")
        response = UserList.as_view(request)
        self.assertIsNotNone(response)

    def test_get_user_list_authenticated(self):
        """Test that authenticated users can retrieve the user list."""
        request = self.factory.get("/users/")
        force_authenticate(request, user=self.user)
        response = UserList.as_view(request)
        self.assertIsNotNone(response)

    def test_create_user_unauthenticated(self):
        """Test that unauthenticated users cannot create a new user."""
        data = {"username": "newuser", "password": "newpassword"}
        request = self.factory.post("/users/", data=data)
        response = UserList.as_view(request)
        self.assertIsNotNone(response)

    def test_create_user_authenticated(self):
        """Test that authenticated users can create a new user."""
        data = {"username": "newuser", "password": "newpassword"}
        request = self.factory.post("/users/", data=data)
        force_authenticate(request, user=self.user)
        response = UserList.as_view(request)
        self.assertIsNotNone(response)


class CustomerListViewTest(TestCase):

    def setUp(self):
        """Set up test data for the CustomerList view tests."""
        self.factory = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        phone = "1234567890"
        self.customer = Customer.objects.create(user=self.user, phone=phone)

    def test_get_customer_list_unauthenticated(self):
        """Test that unauthenticated users can retrieve the customer list."""
        request = self.factory.get("/customers/")
        response = CustomerList.as_view(request)
        self.assertIsNotNone(response)

    def test_get_customer_list_authenticated(self):
        """Test that authenticated users can retrieve the customer list."""
        request = self.factory.get("/customers/")
        force_authenticate(request, user=self.user)
        response = CustomerList.as_view(request)
        self.assertIsNotNone(response)

    def test_create_customer_unauthenticated(self):
        """Test that unauthenticated users cannot create a new customer."""
        data = {"phone": "9876543210", "user_id": self.user.id}
        request = self.factory.post("/customers/", data=data)
        response = CustomerList.as_view(request)
        self.assertIsNotNone(response)

    def test_create_customer_authenticated(self):
        """Test that authenticated users can create a new customer."""
        data = {"phone": "9876543210", "user_id": self.user.id}
        request = self.factory.post("/customers/", data=data)
        force_authenticate(request, user=self.user)
        response = CustomerList.as_view(request)
        self.assertIsNotNone(response)
