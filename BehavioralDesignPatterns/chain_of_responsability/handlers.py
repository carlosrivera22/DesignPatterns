from abstract_handler import AbstractHandler
from request import Request

class Handler1(AbstractHandler):
    def handle(self, request):
        if request.getValue() < 0:
            print("Handler1 handles negative values.")
            print("\tHandler1.handle: " + request.getDescription() + str(request.getValue()))
            print()
        else:
            super().handle(request)
        

class Handler2(AbstractHandler):
    def handle(self, request):
        if request.getValue() == 0:
            print("Handler2 handles zero values.")
            print("\tHandler2.handle: " + request.getDescription() + str(request.getValue()))
            print()
        else:
            super().handle(request)


class Handler3(AbstractHandler):
    def handle(self, request):
        if request.getValue() > 0:
            print("Handler3 handles positive values.")
            print("\tHandler3.handle: " + request.getDescription() + str(request.getValue()))
            print()
        else:
            super().handle(request)
