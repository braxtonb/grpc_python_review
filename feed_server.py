import logging
import grpc
from concurrent import futures

from feed_pb2_grpc import FeedServiceServicer, add_FeedServiceServicer_to_server
from feed_pb2 import Feed, Article, GetFeedResponse, GetFeedRequest, GetArticleByIdRequest, GetArticleByIdResponse
from animal_pb2_grpc import AnimalServiceServicer, add_AnimalServiceServicer_to_server
from animal_pb2 import Animal, GetAnimalsResponse, GetAnimalsRequest, GetAnimalByIdRequest, GetAnimalByIdResponse


articles = [
    Article(id=0, title='First article'),
    Article(id=1, title='Second article'),
    Article(id=2, title='Third article'),
]

animals = [
    Animal(id=0, name='First animal'),
    Animal(id=1, name='Second animal'),
    Animal(id=2, name='Third animal'),
]


class FeedServer(FeedServiceServicer):
    def __init__(self):
        pass

    def GetFeed(self, request: GetFeedRequest, context):
        feed = Feed(articles=articles)

        return GetFeedResponse(feed=feed)

    def GetArticleById(self, request: GetArticleByIdRequest, context):
        try:
            return GetArticleByIdResponse(
                article=articles[request.id]
            )
        except:
            logging.exception(f'Unable to find article by id {request.id}')


class AnimalServer(AnimalServiceServicer):
    def __init__(self):
        pass

    def GetAnimals(self, request: GetAnimalsRequest, context):
        return GetAnimalsResponse(animals=animals)

    def GetAnimalById(self, request: GetAnimalByIdRequest, context):
        try:
            return GetAnimalByIdResponse(
                animal=animals[request.id]
            )
        except:
            logging.exception(f'Unable to find animal by id {request.id}')


PORT = 50051


def serve():
    print('Starting server...')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_FeedServiceServicer_to_server(
        FeedServer(), server
    )
    add_AnimalServiceServicer_to_server(
        AnimalServer(), server
    )
    server.add_insecure_port(f'[::]:{PORT}')
    server.start()
    print('Server started on port {PORT}...')
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()