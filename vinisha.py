lass mynum():

    def __iter__(self):

        self.a=1

        return self

    def __next__(self):

        x=self.a

        self.a +=1

        return x

myclass=mynum()

myiter=iter(myclass)

print(next(myclass))

print(next(myclass))

print(next(myclass))

print(next(myclass))

print(next(myclass))

print(next(myclass))

print(next(myclass))

print(next(myclass))

print(next(myclass))

print(next(myclass))
