from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'Luciano da Cunha',
            cpf = '11111111111',
            email = 'luciano@email.com',
            phone = '19-99999-9999',
        )

        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Luciano da Cunha', str(self.obj))

    def test_paid_default_to_false(self):
        """By default paid must be False."""
        self.assertEqual(False, self.obj.paid)