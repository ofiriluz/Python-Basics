# abc standard library is a collection of decorators for abstract classes
# It is mainly used for abstracting different methods or static methods
# Once the decorator is used, an exception will be thrown if the method will not be overwritten
import abc

class BaseRequest(object):
    def __init__(self):
        pass

    @abc.abstractmethod
    def method(self):
        pass

    @abc.abstractmethod
    def api_path(self):
        pass

    @abc.abstractmethod
    def data(self):
        pass

    @staticmethod
    @abc.abstractstaticmethod
    def name():
        pass