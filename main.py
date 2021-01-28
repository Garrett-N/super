from LoggingDict import LoggingDict, LoggingOD
from pprint import pprint
import logging


# for my examples, i want to see INFO in console output
logging.basicConfig(level=logging.DEBUG)

my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

log_dict = LoggingDict(my_dict)
ordered_dict = LoggingOD(my_dict)

my_dict.__setitem__('color', 'red')
log_dict.__setitem__('color', 'blue')
ordered_dict.__setitem__('color', 'yellow')

pprint(LoggingOD.__mro__)