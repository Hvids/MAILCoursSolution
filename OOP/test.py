from abc import ABC, abstractmethod

class ObservableEngine(Engine):
    
    def __init__(self):
        self.__subscribers = set()
    
    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)
    
    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)
    

    def notify(self, message):
        for sub in self.__subscribers:
            sub.update(message)

class AbstractObserver(ABC):            
        @abstractmethod
        def update(self, achieve):
            pass

class ShortNotificationPrinter(AbstractObserver):
    def __init__ (self):
        
        self.achievements = set()

    def update(self, achieve):
        achieve = tuple(achieve.values())
        if not achieve in self.achievements:
            self.achievements.add(achieve)    
       
        
class FullNotificationPrinter(AbstractObserver):
    def __init__ (self):
        self.achievements = list()
        
    def update(self, achieve):
        achieve = tuple(achieve.values())
        if not achieve in self.achievements:
            self.achievements.append(achieve)