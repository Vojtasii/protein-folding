from ComplexNumber import ComplexNumber


if __name__ == "__main__":
    a = ComplexNumber(1, 1)
    b = ComplexNumber(1, 1)
    size_of_a = a.size() # size of the complex number
    c = a*b # c must be also a Lesson2 object, use __add__
    print(size_of_a)
    print(c.re,c.im) # just a simple check that the addition works
    print(c) # implement simple __str__ method
    #print(ComplexNumber(0, 1))
    #print(ComplexNumber(1, 0))
