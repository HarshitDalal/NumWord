import unittest

from Logs import LoggerConfig
from NumWord import Currency
import os


class TestCurrency(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = LoggerConfig(__name__).get_logger()
        cls.logger.info("TestCurrency started.")
        cls.currency = Currency()

    @classmethod
    def tearDownClass(cls):
        cls.logger.info("TestCurrency completed. \n -----------------")

    def test_currency_conversion_valid(self):

        result = self.currency.convert(100, "USD", "EUR", with_symbol=False)
        self.assertIsInstance(result, str)
        self.logger.info(f"Test Convert 100 USD to EUR without symbol -> {result}")
        self.assertTrue("EUR" in result)

        result = self.currency.convert(50, "EUR", "INR", with_symbol=True)
        self.assertIsInstance(result, str)
        self.logger.info(f"Test Convert 50 EUR to INR with symbol -> {result}")
        self.assertTrue("₹" in result)

    def test_invalid_currency(self):
        self.logger.info("Test Invalid Currency Code")
        with self.assertRaises(ValueError):
            self.currency.convert(100, "USD", "XYZ", with_symbol=True)  # Invalid currency code

    def test_load_exchange_rates_from_file(self):
        rates = self.currency._Currency__rates
        self.assertIsInstance(rates, dict)
        self.logger.info(f"Test Exchange rates load successfully: Total rates found -> {len(rates)}")
        self.assertGreater(len(rates), 0)

    def test_exchange_rates_file_persistence(self):
        old_currency_data = self.currency._Currency__load_exchange_rates()

        currency_data = {"date": "2025-02-07", "rates": {"USD": 1.0, "EUR": 0.85}, "Base": "USD"}
        self.currency._Currency__save_exchange_rates(currency_data)

        file_path = self.currency._Currency__FILE_NAME
        self.logger.info("Test exchange rate file available or not")
        self.assertTrue(os.path.exists(file_path))

        loaded_data = self.currency._Currency__load_exchange_rates()

        self.logger.info(f"Test USD Exchange Rates -> {loaded_data['rates']['USD']}")
        self.assertEqual(loaded_data["rates"]["USD"], 1.0)
        self.logger.info(f"Test EUR Exchange Rates -> {loaded_data['rates']['EUR']}")
        self.assertEqual(loaded_data["rates"]["EUR"], 0.85)

        self.currency._Currency__save_exchange_rates(old_currency_data)

    def test_fetch_exchange_rates(self):

        data = self.currency._Currency__fetch_exchange_rates()
        self.logger.info(f"Test Base Code is USD -> {data['Base']}")
        self.assertEqual(data["Base"], "USD")
        self.assertGreater(len(data["rates"]), 0)

    def test_currency_conversion_with_live_data(self):

        self.logger.info(f"Test Cases with live exchange rates")
        result = self.currency.convert(100, "USD", "EUR", with_symbol=False)
        self.assertIsInstance(result, str)
        self.assertTrue("EUR" in result)

        result = self.currency.convert(100, "USD", "EUR", with_symbol=True)
        self.assertIsInstance(result, str)
        self.assertTrue("€" in result)


if __name__ == '__main__':
    unittest.main()
