# This is a python file! The '#' character indicates that the following line is a comment.

# The following is an example for how to define a function in Python
# def tells the compiler that hello_world is the name of a function
# this implementation of hello_world takes a string as an argument,
# which has default value of the empty string. If the user calls
# hello_world() without an argument, then the compiler uses ''
# as the default value of the argument.
def hello_world(name=''):
    print "hello world!"
    print name
    return

hello_world()

def Riemann(a,b,N):
    delta = (b-a)/N
    x = a + delta
    area = 0
    while x <= b:
        y = x**2
        area = area + (y*delta)
        x = x + delta
    print area

Riemann(0,10,10000.)




#Implement the Riemann Sum approximation for integrals.
