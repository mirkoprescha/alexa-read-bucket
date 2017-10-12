# coding=UTF-8

text = """
#heeute ist ein schöner Tag. Wort A.
WortB.

# Warum ist das so?

# wieso!

"""

a = text.split('#')
print "QWERT" + a[1]
print a
for i in a:
    print i

