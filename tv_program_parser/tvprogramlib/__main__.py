import sys
from .content_manager import ContentManager
from .api_client import TvMazeClient

if __name__ == "__main__":
    query = " ".join(sys.argv[1:])

    assert query, "query string was not provided"

    manager = ContentManager(
        search_query=query, client=TvMazeClient()
    )
    manager.get_content()
    result = manager.format_content()
    print(result)
