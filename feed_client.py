import logging
import grpc

from feed_pb2_grpc import FeedServiceStub
from feed_pb2 import GetArticleByIdRequest, GetFeedRequest
from animal_pb2_grpc import AnimalServiceStub
from animal_pb2 import GetAnimalByIdRequest, GetAnimalsRequest

from feed_server import PORT


class FeedClient:
    def __init__(self, stub: FeedServiceStub):
        self._stub = stub

    def get_feed(self):
        print("-------------- GetFeed --------------")
        feed = self._stub.GetFeed(
            GetFeedRequest()
        )

        print(f'{feed=}')

    def get_article_by_id(self, id: int):
        print("-------------- GetArticleById --------------")
        article = self._stub.GetArticleById(
            GetArticleByIdRequest(id=id)
        )

        print(f'{article=}')

    def make_requests(self):
        print("-------------- Start FeedClient --------------")
        self.get_feed()
        self.get_article_by_id(1)
        print("-------------- End FeedClient --------------")



class AnimalClient:
    def __init__(self, stub: AnimalServiceStub):
        self._stub = stub

    def get_animals(self):
        print("-------------- GetAnimals --------------")
        animals = self._stub.GetAnimals(
            GetAnimalsRequest()
        )

        print(f'{animals=}')

    def get_animal_by_id(self, id: int):
        print("-------------- GetAnimalById --------------")
        animal = self._stub.GetAnimalById(
            GetAnimalByIdRequest(id=id)
        )

        print(f'{animal=}')

    def make_requests(self):
        print("-------------- Start AnimalClient --------------")
        self.get_animals()
        self.get_animal_by_id(1)
        print("-------------- End AnimalClient --------------")


def run():
    with grpc.insecure_channel(f'localhost:{PORT}') as channel:
        feed_client = FeedClient(
            stub=FeedServiceStub(channel)
        )
        animal_client = AnimalClient(
            stub=AnimalServiceStub(channel)
        )

        feed_client.make_requests()
        animal_client.make_requests()


if __name__ == '__main__':
    logging.basicConfig()
    run()
