
from unittest import TestCase
from unittest.mock import patch, MagicMock

from tests.stub import NetworkTrafficProviderStub
from src.domain.dtos.network_traffic_average_speed import NetworkTrafficAverageSpeedDTO
from src.domain.models.response.read_network_traffic_average_speed_response_model import ReadNetworkTrafficAverageSpeedResponseModel
from src.domain.use_cases.network_traffic.read_network_traffic_average_speed import ReadNetworkTrafficAverageSpeed


@patch("src.domain.use_cases.network_traffic.read_network_traffic_average_speed.read_network_traffic_average_speed.NetworkTraffic")
class ReadNetworkTrafficAverageSpeedTestCase(TestCase):

    def setUp(self) -> None:
        self._stub_provider = NetworkTrafficProviderStub()

    def test_should_read_network_traffic_average_speed(self, mock_network_traffic: MagicMock):
        mock_network_traffic.return_value = self._stub_provider

        use_case = ReadNetworkTrafficAverageSpeed()

        actual = use_case.execute()

        network_traffic_data = self._stub_provider.get_data()
        data = network_traffic_data[0]
        average_speed_response = NetworkTrafficAverageSpeedDTO(
            pid=data.pid,
            name=data.name,
            average_download_speed=78.0,
            average_upload_speed=0.0,
            last_time_update=data.last_time_update,
            create_time=data.create_time,
            downloads=[78.0, 78.0, 78.0],
            uploads=[0.0, 0.0, 0.0]
        )
        average_speeds = [average_speed_response]
        expected = ReadNetworkTrafficAverageSpeedResponseModel(average_speeds)

        self.assertEqual(actual, expected)

    def test_should_read_network_traffic_data_when_provider_returns_empty_list(
        self,
        mock_network_traffic: MagicMock
    ):
        mock_network_traffic.return_value.get_data.return_value = []

        use_case = ReadNetworkTrafficAverageSpeed()

        actual = use_case.execute()
        expected = ReadNetworkTrafficAverageSpeedResponseModel(traffic_speed_averages=[])

        self.assertEqual(actual, expected)
