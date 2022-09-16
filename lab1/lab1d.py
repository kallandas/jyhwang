#!/usr/bin/env python3
'''Description: This program will output "10 + 2 * 5 = 20" to the screen.'''

# Any line that starts with a "#" is also known as a comment,
# these lines are ignored by the python interpreter even if
# they contain code. The very first line is called a SheBang line,
# it is used to tell the system which interpreter to
# use(python2, python3, bash, etc).

x = 10
y = 2
z = 5
result = x + y * z
print(str(x) + ' + ' + str(y) + ' * ' + str(z) + ' = ' + str(result))
