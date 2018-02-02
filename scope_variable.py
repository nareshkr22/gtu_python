#Write a program that demonstrates scope of variable in nested functions

def f(x):
    x=1
    def g():
        x=2
        print("inside g ....x= ",x)
    def h():
        z=x
        print("inside h .... z= ",z)
   
    print("inside f before functions h and g .... x= ",x)
    h();
    g();
    print("inside f after functions h and g.... x= ",x)
    return g



x=1
z=func(x)
print("main x= ",x)
print("main z= ",z)
z()
        
            