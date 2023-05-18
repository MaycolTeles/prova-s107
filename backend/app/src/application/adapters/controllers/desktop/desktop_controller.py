"""
Module containing the "DesktopController" Class.
"""

from application.adapters.presenters.desktop import DesktopPresenter
from domain.use_cases.network_traffic.read_network_traffic_data import ReadNetworkTrafficData


class DesktopController:
    """
    TODO
    """
    _presenter: DesktopPresenter

    def __init__(self) -> None:
        """
        TODO
        """
        self._presenter = DesktopPresenter()

    def get_network_traffic_data(self):
        """
        TODO
        """
        use_case = ReadNetworkTrafficData()
        response = use_case.execute()

        desktop_response = self._presenter.present_network_traffic_data(response) 

        return desktop_response

    def save_chart(self):
        """"""
        return "saving chart"

    def export_chart(self):
        """"""
        return "exporting chart"
