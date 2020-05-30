
# Ensure that only one instance of a class is created

class Singleton:
    instance = None

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.instance = self

    @staticmethod 
    def getInstance():
        """ Static access method. """
        if Singleton.instance == None:
            Singleton()
        return Singleton.instance
   

# Sometimes it is important to have only one instance of a class.

# For example, in a system where there should be only one window manager.

# Usually Singletons are used for centralized management of internal or 
# external resources and they provide a global point of access to themselves.
s = Singleton()
print(s)

s = Singleton.getInstance()
print(s)

s = Singleton.getInstance()
print(s)
