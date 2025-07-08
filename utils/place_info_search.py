from langchain_tavily import TavilySearch
import requests

from dotenv import load_dotenv
import os

class GooglePlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.fsq_api_key = os.getenv("fsq_api_key")
        self.geoapify_key = os.getenv("GEOAPIFY_API_KEY")
        

    def fsq_search(self, query: str, near: str) -> dict:
        url = "https://api.foursquare.com/v3/places/search"
        headers = {
            "Accept": "application/json",
            "Authorization": self.fsq_api_key
        }
        params = {
            "query": query,
            "near": near,
            "limit": 10
        }
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def geoapify_transport_search(self, place: str) -> dict:
        url = "https://api.geoapify.com/v2/places"
        params = {
            "categories": "transport",
            "filter": f"place:{place}",
            "limit": 10,
            "apiKey": self.geoapify_key
        }
        response = requests.get(url, params=params)
        return response.json()

    def google_search_attractions(self, place: str) -> dict:
        return self.fsq_search("attractions", place)

    def google_search_restaurants(self, place: str) -> dict:
        return self.fsq_search("restaurants", place)

    def google_search_activity(self, place: str) -> dict:
        return self.fsq_search("activities", place)

    def google_search_transportation(self, place: str) -> dict:
        return self.geoapify_transport_search(place)

    
class TavilyPlaceSearchTool:
    def __init__(self):
        pass

    def tavily_search_attractions(self, place: str) -> dict:
        """
        Searches for attractions in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"top attractive places in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_restaurants(self, place: str) -> dict:
        """
        Searches for available restaurants in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"what are the top 10 restaurants and eateries in and around {place}."})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_activity(self, place: str) -> dict:
        """
        Searches for popular activities in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"activities in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_transportation(self, place: str) -> dict:
        """
        Searches for available modes of transportation in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"What are the different modes of transportations available in {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result


