from django.test import TestCase
from .pricing_engine import calculate_fare

class PricingTests(TestCase):
    def test_standard_fare(self):
        fare = calculate_fare(5, 'low', 'normal')
        self.assertEqual(fare["total_fare"], 7.5)

    def test_high_traffic_pricing(self):
        fare = calculate_fare(8, 'high', 'normal')
        self.assertEqual(fare["traffic_multiplier"], 1.5)

    def test_surge_pricing(self):
        fare = calculate_fare(12, 'normal', 'peak')
        self.assertEqual(fare["demand_multiplier"], 1.8)

    def test_peak_hour_high_traffic(self):
        fare = calculate_fare(7, 'high', 'peak')
        self.assertTrue(fare["total_fare"] > 20)
