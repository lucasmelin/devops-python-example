from decimal import Decimal

from django.test import TestCase
from records.models import Commodity


class CommodityTestCase(TestCase):
    def setUp(self):
        Commodity.objects.create(name="Purple Avocadoes", value=0.2)

    def test_commodity_exists(self):
        """
        Verify that the commodity created in the setUp exists with the correct value.
        """
        avocado = Commodity.objects.get(name="Purple Avocadoes")
        self.assertEqual(avocado.value, Decimal("0.2"))
