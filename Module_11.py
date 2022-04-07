from collections import UserDict
import datetime


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self.value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        print(type(value))
        if type(value) == str:
            self.__value = value
            print(type(value))


class Name(Field):
    pass


class Birthday(Field):

    @Field.value.setter
    def value(self, value):
        try:
            valid_data = datetime.datetime.strptime(value, '%Y-%m-%d')
            if datetime.datetime.now() > valid_data or \
                    datetime.datetime.now().year+1 < valid_data.year:
                raise ValueError
            Field.value.fset(self, value)
        except ValueError:
            print('Enter correct, actual and exist date in format yyyy-mm-dd.')


class Phone(Field):
    @Field.value.setter
    def value(self, value):
        try:
            if not value.isdigit() or 8 > len(value) < 20:
                raise ValueError()
            Field.value.fset(self, value)
        except ValueError:
            print('Enter phone only using digital characters')


class Record:
    def __init__(self, name: Name, birthday=None, *args: Phone):
        self.name = name
        self.phones = []
        self.birthday = birthday
        for phone in args:
            self.phones.append(phone)

    def __str__(self):
        if len(self.phones) > 0:
            return f"Your record Name: {self.name} Phones: {self.phones}"
        return f"Your record Name: {self.name}"

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def add_birthday(self, birthday: Birthday):
        self.birthday = birthday

    def delete_phone(self, phone: Phone):
        self.phone.remove(phone)

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        self.add_phone(new_phone)
        self.delete_phone(old_phone)

    def days_to_birthday(self):
        if self.birthday:
            datetime_now = datetime.datetime.now().date()
            birthday_user = datetime.datetime.strptime(self.birthday,
                                                       '%Y-%m-%d').date()
            result = (datetime_now - birthday_user).days
            return abs(result)
        return "You don't enter birthdate, please add "


class AddressBook(UserDict):

    def __init__(self):
        self.data = {}

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def iterator(self, n):
        counter = 0
        result_string = ''
        for key, value in self.data.items():
            counter +=1
            if counter == n+1:
                yield result_string
            result_string += str(value) + '\n'