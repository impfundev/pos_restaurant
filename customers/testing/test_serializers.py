from django.test import TestCase
from customers.models import User, Customer
from customers.serializers import UserSerializer, CustomerSerializer


class CustomerSerializerTest(TestCase):

    def setUp(self):
        """Set up test data for the serializer tests."""
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        phone = "1234567890"
        self.customer = Customer.objects.create(user=self.user, phone=phone)

    def test_user_serializer_valid_data(self):
        """Test that the UserSerializer can serialize valid data."""
        serializer = UserSerializer(self.user)
        self.assertEqual(serializer.data["username"], "testuser")
        self.assertEqual(
            serializer.data["email"], ""
        )  # Assuming email is empty in the test user
        self.assertEqual(
            serializer.data["first_name"], ""
        )  # Assuming first_name is empty in the test user
        self.assertEqual(
            serializer.data["last_name"], ""
        )  # Assuming last_name is empty in the test user

    def test_customer_serializer_valid_data(self):
        """Test that the CustomerSerializer can serialize valid data."""
        serializer = CustomerSerializer(self.customer)
        self.assertEqual(serializer.data["phone"], "1234567890")
        self.assertEqual(serializer.data["user_id"], self.user.id)

    def test_customer_serializer_update(self):
        """
        Test that the CustomerSerializer can update an
        existing Customer object.
        """
        data = {"phone": "5551234567", "user_id": self.user.id}
        serializer = CustomerSerializer(self.customer, data=data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.phone, "5551234567")
