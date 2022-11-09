import logging
from typing import Optional

from api_client import TvMazeClient, ClientError
from models import TvProgramModel

logger = logging.getLogger(__name__)


class ContentManager:
    def __init__(self, search_query, client: TvMazeClient):
        self.search_query = search_query
        self.client = client
        self.content: Optional[TvProgramModel] = None

    def get_content(self):
        try:
            self.content = self.client.search(self.search_query)
        except ClientError:
            logging.exception("Could not get content from client")

    def format_content(self) -> str:
        assert self.content, "get_content() should be called first"

        result = (
            f"Name: {self.content.name}\n"
            f"Network Name: {self.content.network.name}\n"
            f"Network Country Name: {self.content.network.country.name}\n"
            f"Summary: {self.content.summary}"
        )

        return result
