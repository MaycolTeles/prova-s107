
from unittest import TestCase
from unittest.mock import patch, MagicMock

from tests.stub import NetworkTrafficProviderStub
from src.application.infra.ui.rest.web.flask_ui import FlaskUI


class APITestCase(TestCase):

    def setUp(self) -> None:
        flask = FlaskUI()
        self._test_client = flask._flask.test_client()

    def test_should_read_index(self):
        response = self._test_client.get('/api')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

    def test_should_get_network_traffic_data(self):
        patcher_network_provider = patch("src.domain.entities.network_traffic.network_traffic.network_traffic_provider_factory")
        mock: MagicMock = patcher_network_provider.start()
        mock.return_value = NetworkTrafficProviderStub()

        response = self._test_client.get('/api/network-traffic-data')

        self.assertEqual(response.status_code, 200)

        actual = response.data
        expected = (
            b'{"network_traffic_data":[{"create_time":"16/05/2023, 08:18:24","download":"4.19MB","download_speed":"78.00B/s","host_traffic":[{"download":"133.08KB","host":"10.0.16.31","upload":"0.00B"}],"last_time_update":"16/05/2023, 20:04:40","name":"snapd","pid":"634","protocol_traffic":[{"download":"133.08KB","protocol":"others","upload":"0.00B"}],"upload":"0.00B","upload_speed":"0.00B"}]}\n'
        )

        self.assertEqual(actual, expected)

    def test_should_get_network_traffic_average_speed(self):
        patcher_network_provider = patch("src.domain.entities.network_traffic.network_traffic.network_traffic_provider_factory")
        mock: MagicMock = patcher_network_provider.start()
        mock.return_value = NetworkTrafficProviderStub()

        response = self._test_client.get('/api/network-traffic-average-speed')

        self.assertEqual(response.status_code, 200)

        actual = response.data
        expected = (
            b'{"traffic_speed_averages":[{"average_download_speed":78.0,"average_upload_speed":0.0,"create_time":"16/05/2023, 08:18:24","downloads":[78.0,78.0,78.0],"last_time_update":"16/05/2023, 20:04:40","name":"snapd","pid":"634","uploads":[0.0,0.0,0.0]}]}\n'
        )

        self.assertEqual(actual, expected)

    def test_should_get_invalid_endpoint(self):
        response = self._test_client.get('/api/test-invalid-endpoint')

        self.assertEqual(response.status_code, 404)

        actual = response.data
        expected = (
            b'<!doctype html>\n<html lang=en>\n<title>404 Not Found</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>\n'
        )

        self.assertEqual(actual, expected)
