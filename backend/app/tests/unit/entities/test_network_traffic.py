
from unittest import TestCase
from unittest.mock import patch, MagicMock

from tests.stub import NetworkTrafficProviderStub
from src.domain.entities.network_traffic.network_traffic import NetworkTraffic


@patch("src.domain.entities.network_traffic.network_traffic.network_traffic_provider_factory")
class NetworkTrafficTestCase(TestCase):

    def setUp(self) -> None:
        self._network_traffic_data_provider = NetworkTrafficProviderStub()

    def test_should_get_network_traffic_data_from_provider(self, mock_factory: MagicMock) -> None:
        mock_factory.return_value = self._network_traffic_data_provider

        network_traffic = NetworkTraffic()
        network_traffic_data = network_traffic.get_data()

        actual = network_traffic_data
        expected = self._network_traffic_data_provider.get_data()

        self.assertEqual(actual, expected)

    def test_should_get_network_traffic_data_package_from_provider(self, mock_factory: MagicMock) -> None:
        mock_factory.return_value = self._network_traffic_data_provider

        network_traffic = NetworkTraffic()
        network_traffic_data = network_traffic.get_data_package()

        actual = network_traffic_data
        expected = self._network_traffic_data_provider.get_data_package()

        self.assertEqual(actual, expected)
