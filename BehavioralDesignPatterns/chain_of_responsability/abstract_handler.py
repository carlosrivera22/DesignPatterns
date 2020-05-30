from abc import ABC, abstractmethod
class AbstractHandler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """
    _next_handler= None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    
    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)

        return None