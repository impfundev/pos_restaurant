from customers.models import User, Customer
from django.test import TestCase


# Create your models here.
class CustomerModelTest(TestCase):

    def setUp(self):
        """Set up a test user for the tests."""
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

    def test_customer_creation(self):
        """Test that a Customer object can be created."""
        customer = Customer.objects.create(user=self.user, phone="1234567890")
        self.assertIsInstance(customer, Customer)

    def test_customer_has_user(self):
        """Test that a Customer object has a user associated with it."""
        customer = Customer.objects.create(user=self.user, phone="1234567890")
        self.assertEqual(customer.user, self.user)

    def test_customer_has_phone(self):
        """Test that a Customer object has a phone number."""
        customer = Customer.objects.create(user=self.user, phone="1234567890")
        self.assertEqual(customer.phone, "1234567890")

    def test_customer_db_table_name(self):
        """Test that the Customer model has the correct database table name."""
        self.assertEqual(Customer._meta.db_table, "customer")
