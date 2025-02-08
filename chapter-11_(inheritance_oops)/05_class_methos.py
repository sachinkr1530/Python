class employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")
        
e=employee()
e.a=45
e.show()
        