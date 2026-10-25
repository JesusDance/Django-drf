import httpx
from .logger import logger
from django_start import settings

class FootballClient:
    def __init__(self, url: str, api_key: str = settings.API_KEY):
        self.url = url
        self.api_key = api_key

    def fetch_team(self, team_id: int) -> dict:
        try:
            params = {
                "team_id": team_id,
                "action": "get_teams",
                "APIkey": self.api_key,
            }
            with httpx.Client() as client:
                logger.info("Fetching data from external API", extra={"team_id": team_id})
                response = client.get(url=self.url, params=params, timeout=10)
                response.raise_for_status()
                data = response.json()
                if not data:
                    raise ...
                return {
                    "name": data[0].get("team_name"),
                    "team_id": team_id,
                    "country": data[0].get("team_country"),
                }
        except httpx.TimeoutException:
            raise TimeoutError({"timeout": "Timeout exception"})


    def __str__(self):
        return f"{self.url}"

    def __repr__(self):
        return f"FootballClient(url={self.url}"
