import grpc
from concurrent import futures
from proto import IsAllowed_pb2 as pb2, IsAllowed_pb2_grpc as pb2_grpc


class UnaryService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass


    def GetServerResponse(self, request, context):
        logins = {1: 'admin', 2: 'andrey'}
        print(request.name)
        result = {'isAllowed': self.CheckName(request.name, logins)}

        return pb2.IsAllowedReply(**result)


    def CheckName(self, name, logins):
        values = logins.values()
        if name in values:
            flag = True
        else:
            flag = False
        print(name)
        return flag


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
