class CreateObjectError(Exception):
    """ create object error. """

    def __init__(self, class_name: str, *args, **kwargs):  # real signature unknown
        self.class_name = class_name

    def __str__(self, *args, **kwargs):  # real signature unknown
        """ Return str(self). """
        return '%s类不能被创建为对象。' % self.class_name


class PassengerError(Exception):

    def __init__(self, passenger_name: str, *args, **kwargs):  # real signature unknown
        self.passenger_name = passenger_name

    def __str__(self, *args, **kwargs):  # real signature unknown
        """ Return str(self). """
        return '%s信息缺失。' % self.passenger_name


class MyError(Exception):

    def __init__(self, error_messages: str, *args, **kwargs):  # real signature unknown
        self.error_messages = error_messages

    def __str__(self, *args, **kwargs):  # real signature unknown
        """ Return str(self). """
        return self.error_messages
