import json
from abc import ABC, abstractmethod
from pathlib import Path
from uuid import uuid4


class BaseStorage(ABC):

    @abstractmethod
    def create_travel_agency(self, travel_agency: dict):
        pass

    @abstractmethod
    def get_travels_agency(self, skip: int = 0, limit: int = 10, search_param: str = ''):
        pass

    @abstractmethod
    def get_travel_agency_info(self, travel_agency_id: str):
        pass

    @abstractmethod
    def update_travel_agency(self, travel_agency_id: str, country_travel: str):
        pass

    @abstractmethod
    def delete_travel_agency(self, travel_agency_id: str):
        pass


class JSONStorage(BaseStorage):
    def __init__(self):
        self.file_name = 'storage.json'

        my_file = Path(self.file_name)
        if not my_file.is_file():
            with open(self.file_name, mode='w', encoding='utf-8') as file:
                json.dump([], file, indent=4)

    def create_travel_agency(self, travel_agency: dict):
        with open(self.file_name, mode='r') as file:
            content: list[dict] = json.load(file)

        travel_agency['id'] = uuid4().hex
        content.append(travel_agency)
        with open(self.file_name, mode='w', encoding='utf-8') as file:
            json.dump(content, file, indent=4)
        return travel_agency

    def get_travels_agency(self, skip: int = 0, limit: int = 10, search_param: str = ''):
        with open(self.file_name, mode='r') as file:
            content: list[dict] = json.load(file)

        if search_param:
            data = []
            for travel_agency in content:
                if search_param in travel_agency['country_travel']:
                    data.append(travel_agency)
            sliced = data[skip:][:limit]
            return sliced

        sliced = content[skip:][:limit]
        return sliced

    def get_travel_agency_info(self, travel_agency_id: str):
        with open(self.file_name, mode='r') as file:
            content: list[dict] = json.load(file)

        for travel_agency in content:
            if travel_agency_id == travel_agency['id']:
                return travel_agency
        return {}

    def update_travel_agency(self, travel_agency_id: str, country_travel: str):
        with open(self.file_name, mode='r') as file:
            content: list[dict] = json.load(file)

        was_found = False
        for travel_agency in content:
            if travel_agency['id'] == travel_agency['id']:
                travel_agency['country_travel'] = country_travel
                was_found = True
                break
        if was_found:
            with open(self.file_name, mode='w', encoding='utf-8') as file:
                json.dump(content, file, indent=4)
        raise ValueError()

    def delete_travel_agency(self, travel_agency_id: str):
        with open(self.file_name, mode='r') as file:
            content: list[dict] = json.load(file)

        was_found = False
        for travel_agency in content:
            if travel_agency_id == travel_agency['id']:
                content.remove(travel_agency)
                was_found = True
                break
        if was_found:
            with open(self.file_name, mode='w', encoding='utf-8') as file:
                json.dump(content, file, indent=4)
        raise ValueError()


storage = JSONStorage()
