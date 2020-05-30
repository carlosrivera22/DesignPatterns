from abstract_observer import Observer

class ConcreteObserverA(Observer):
    def update(self, subject):
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject):
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")
