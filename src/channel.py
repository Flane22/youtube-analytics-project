import json
import os
from pprint import pprint

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('YT_API_KEY')
    __youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = self.__youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        pprint(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self, file_name):
        data = json.dumps(self.channel)
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(data)

    @property
    def title(self):
        return self.channel['items'][0]['snippet']['title']

    @property
    def video_count(self):
        return int(self.channel['items'][0]['statistics']['videoCount'])

    @property
    def url(self):
        return self.channel['items'][0]['snippet']['thumbnails']['default']['url']

    @property
    def description(self):
        return self.channel["items"][0]["snippet"]["description"]

    @property
    def subscriber_count(self):
        return int(self.channel["items"][0]["statistics"]["subscriberCount"])

    @property
    def view_count(self):
        return int(self.channel["items"][0]["statistics"]["viewCount"])

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        return cls.__youtube

    def __str__(self):
        return f"{self.title} {self.url}"

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return self.subscriber_count - other.subscriber_count

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count

