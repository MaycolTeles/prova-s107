"""
Module containing the "FlaskUI" Class.
"""

from flask import Flask

from .constants import FLASK_SECRET_KEY
from .endpoints import endpoints
from ....interfaces import UI


class FlaskUI(UI):
    """
    Class to represent the User Interface using Flask.
    """
    _flask: Flask

    def __init__(self) -> None:
        """
        Constructor to set up some variables.
        """
        self._flask = Flask(__name__)

    def execute(self) -> None:
        """
        """
        self._configure()
        self._create_routes()

        self._flask.run()

    def _configure(self) -> None:
        """
        """
        self._configure_secret_key()
        self._create_routes()

    def _configure_secret_key(self) -> None:
        """"""
        self._flask.config['SECRET_KEY'] = FLASK_SECRET_KEY

    def _create_routes(self) -> None:
        """
        """
        self._flask.add_url_rule('/', 'index', endpoints.index)
        self._flask.add_url_rule('/network-traffic-data', 'network-traffic-data', endpoints.network_traffic_data)