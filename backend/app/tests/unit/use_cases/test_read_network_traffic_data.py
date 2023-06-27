
from unittest import TestCase
from unittest.mock import patch, MagicMock

from tests.stub import NetworkTrafficProviderStub
from src.domain.use_cases.network_traffic.read_network_traffic_data import ReadNetworkTrafficData
from src.domain.models.response.read_network_traffic_data_response_model import ReadNetworkTrafficDataResponseModel


@patch("src.domain.use_cases.network_traffic.read_network_traffic_data.read_network_traffic_data.NetworkTraffic")
class ReadNetworkTrafficDataTestCase(TestCase):
    
    def setUp(self) -> None:
        self._stub_provider = NetworkTrafficProviderStub()

    def test_should_read_network_traffic_data(self, mock_network_traffic: MagicMock):
        mock_network_traffic.return_value = self._stub_provider

        use_case = ReadNetworkTrafficData()

        actual = use_case.execute()

        network_traffic_data = self._stub_provider.get_data()
        expected = ReadNetworkTrafficDataResponseModel(network_traffic_data)

        self.assertEqual(actual, expected)

    def test_should_read_network_traffic_data_when_provider_returns_empty_list(
        self,
        mock_network_traffic: MagicMock
    ):
        mock_network_traffic.return_value.get_data.return_value = []

        use_case = ReadNetworkTrafficData()

        actual = use_case.execute()
        expected = ReadNetworkTrafficDataResponseModel(network_traffic_data=[])

        self.assertEqual(actual, expected)
