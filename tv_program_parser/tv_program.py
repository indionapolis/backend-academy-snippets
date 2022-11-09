import sys
from content_manager import ContentManager
from api_client import TvMazeClient

if __name__ == "__main__" or __name__ == "tv_program":
    manager = ContentManager(
        search_query=" ".join(sys.argv[1:]), client=TvMazeClient()
    )
    manager.get_content()
    result = manager.format_content()
    print(result)
