# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
listd_ = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(16)]
pprint(listd_)