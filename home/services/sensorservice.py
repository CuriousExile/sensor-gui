from logging import exception
import requests
import json

class SensorApiService:
    API_URL = ""

    def __init__(self, api_url):
        self.API_URL = api_url

    def __generate_time_frame_url(self, start_date, end_date):
        endpoint = "/v1/temperature/range"
        start = "start_date=" + start_date
        end = "end_date=" + end_date
        url = self.API_URL + endpoint + "?" + start + "&" + end
        return url
    
    def pull_temperatures_by_date(self, start_date, end_date):
        url = self.__generate_time_frame_url(start_date, end_date)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                response_text = response.content.decode('utf-8')
                json_data = json.loads(response_text)
                return json_data
            else:
                return [69]
        except exception as e:
            print(f"An error occurred: {e}")
    
    def pull_temperatures(self):
        url = self.API_URL + "/v1/temperature"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                response_text = response.content.decode('utf-8')
                json_data = json.loads(response_text)
                return json_data
            else:
                return [69]
        except exception as e:
            print(f"An error occurred: {e}")

    def get_unique_clients(self):
        data = self.pull_temperatures()
        unique_clients = set()
        for entry in data:
            sourcename = entry.get('sourcename')
            if sourcename:
                unique_clients.add(sourcename)
        return list(unique_clients)