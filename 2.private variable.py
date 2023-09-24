class p:
          name = "Peter"
          __pi=3.141;  #This number is private variable and not show
          def s(self):
                    print("inside the class")
                    print(self.name)
                    print(self.__pi)
a=p()
a.s()
print("outside the class")
print(a.name)
print(a.__pi)
