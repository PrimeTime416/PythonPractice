#
# Example file for working with classes
#


class myClass():

    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2: " + someString)


def main():
    # exercise the class methods
    c = myClass()
    c.method1()
    c.method2("This is a string")
    a = anotherClass()
    a.method2()
    a.method1()


# class 2  declaration
class anotherClass(myClass):

    def method2(self):
        print("anotherClass method2")

    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")


# call main
main()
