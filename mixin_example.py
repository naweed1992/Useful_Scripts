import logging
import json


# Define a LoggingMixin
class LoggingMixin:
    def log(self, message):
        logging.info(f'{self.__class__.__name__}: {message}')


# Define a JSONSerializationMixin
class JSONSerializationMixin:
    def to_json(self):
        return json.dumps(self.__dict__)


# Define a class that uses both mixins
class Person(LoggingMixin, JSONSerializationMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.log('Created new person')


# Create a new Person instance and log its properties to the console
p = Person('John', 30)
p.log(f'{p.name} is {p.age} years old')

# Convert the Person instance to a JSON string
json_string = p.to_json()
print(json_string)
