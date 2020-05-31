# Defines a one-to-many dependency between objects so that when one object changes state,
# all its dependents are notified and updated automatically. 



from subject import ConcreteSubject
from observers import *

if __name__ == "__main__":
    # The client code.

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)
    subject.attach(observer_a)
    subject.some_business_logic()