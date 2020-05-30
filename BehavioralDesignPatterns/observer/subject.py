from abstract_subject import AbstractSubject
from random import randrange
class ConcreteSubject(AbstractSubject):

    _state = None


    _observers = []
 

    def attach(self, observer):
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    

    def notify(self) -> None:
       

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()