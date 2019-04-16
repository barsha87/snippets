from pygoogle import pygoogle
g = pygoogle('cisco')
g.pages = 1
x = g.results()
print x

