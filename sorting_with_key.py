"""
Key Functions. Starting with Python 2.4,
both list.sort() and sorted() added a key parameter
to specify a function to be called on each list element
prior to making comparisons. The value of the key parameter
should be a function that takes a single argument and
returns a key to use for sorting purposes.
"""

a= '17 5 7 43 20 67 90 234 11 200'

b=[int(x) for x in a.split()]
print('b: ', b)

c=sorted(b)
print('c: ', c)

d=sorted(b, key=str)
print('d: ', d)

b.sort(key=str)
print('b: ', b)
