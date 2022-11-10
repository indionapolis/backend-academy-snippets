from typing import Optional, Dict
import requests
from pydantic import ValidationError
from requests import HTTPError, ConnectionError
from logging import getLogger
from .models import TvProgramModel

logger = getLogger(__name__)


def cache(ttl=5 * 60):
    def inner(func):
        def wrapper(*args, **kwargs):
            # TODO cache logic
            result = func(*args, **kwargs)
            return result

        return wrapper

    return inner


class ClientError(Exception):
    pass


class TvMazeClient:
    endpoints = {"search": "singlesearch/shows"}
    api_base = "https://api.tvmaze.com/"

    def _fetch(self, endpoint, params) -> Dict:
        try:
            response = requests.get(
                f"{self.api_base}{endpoint}", params=params
            )
            response.raise_for_status()

            return response.json()
        except HTTPError as e:

            logger.exception("Got unexpected response from server")
            raise ClientError() from e
        except ConnectionError as e:
            logger.exception("Could not connect to server")
            raise ClientError() from e

    @cache(3 * 60)
    def search(self, query: str) -> Optional[TvProgramModel]:
        response_json = self._fetch(self.endpoints["search"], {"q": query})

        result = None
        try:
            result = TvProgramModel(**response_json)
        except ValidationError as e:
            raise ClientError() from e

        return result
