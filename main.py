import grpc
from concurrent import futures
from proto import is_allowed_descriptor_pb2 as pb2, is_allowed_descriptor_pb2_grpc as pb2_grpc
from proto.is_allowed_descriptor_pb2_grpc import IsAllowedService


class IsAllowedService(pb2_grpc.IsAllowedServiceServicer):

    def __init__(self, *args, **kwargs):
        pass


    def send(self, request, context):
        logins = {1: 'admin', 2: 'andrey'}
        print("request.name")
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
    pb2_grpc.add_IsAllowedServiceServicer_to_server(IsAllowedService(), server)
    server.add_insecure_port('[::]:50051')

    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
