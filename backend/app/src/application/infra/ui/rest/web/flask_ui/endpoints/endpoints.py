"""
Module containing all the endpoints for the Flask application.
"""

from flask import Response, jsonify


def index():
    """
    Function to render the index page.
    """
    return Response("Hello, World!")


def network_traffic_data():
    """
    Function to return the network traffic data.
    """
    # instancia caso de uso
    # import ReadAllNetworkTrafficData
    from domain.use_cases.network_traffic.read_all_network_traffic_data import ReadAllNetworkTrafficData
    from dependencies import NETWORK_TRAFFIC_PROVIDER_INJECTION

    NETWORK_TRAFFIC_PROVIDER_INJECTION.start()

    use_case = ReadAllNetworkTrafficData(NETWORK_TRAFFIC_PROVIDER_INJECTION)
    response = use_case.execute()

    return jsonify(response)