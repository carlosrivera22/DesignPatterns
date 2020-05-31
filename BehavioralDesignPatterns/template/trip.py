from abc import ABC, abstractmethod

class Trip(ABC):

    def perform_trip(self):
        self.do_coming_transport()
        self.do_day_a()
        self.do_day_b()
        self.do_day_c()
        self.do_returning_transport()

    @abstractmethod
    def do_coming_transport(self):
        pass

    @abstractmethod
    def do_day_a(self):
        pass

    @abstractmethod
    def do_day_b(self):
        pass

    @abstractmethod
    def do_day_c(self):
        pass

    @abstractmethod
    def do_returning_transport(self):
        pass