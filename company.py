class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, value=None):
        self._first = self.validate_string(value)

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, value=None):
        self._last = self.validate_string(value)


    @staticmethod
    def validate_string(value=None):
        if value is not None:
            if type(value) == str:
                if len(value.strip())<4:
                    raise ValueError('Input must has at least 4 characters')
                else:
                    return value
            else:
                raise ValueError('Input must be a string')
        else:
            raise ValueError('Input cannot be empty')