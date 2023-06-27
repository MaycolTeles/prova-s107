"""
TODO: FIX MODULE
"""

from .constants import UI_INJECTION

from src.application.infra.ui.interfaces import UI
from src.domain.use_cases.network_traffic.interfaces import NetworkTrafficDataProvider


def ui_factory() -> UI:
    """
    """
    from src.application.infra.ui.rest.web.flask_ui import FlaskUI
    from src.application.infra.ui.desktop.tkinter_ui import TkinterUI

    if UI_INJECTION == "Tkinter":
        return TkinterUI()
    
    if UI_INJECTION == "Flask":
        return FlaskUI()

    return FlaskUI()


def network_traffic_provider_factory() -> NetworkTrafficDataProvider:
    """
    """
    from src.application.infra.providers.network_traffic_provider.sockets import SocketIO

    network_traffic_provider = SocketIO()

    return network_traffic_provider
