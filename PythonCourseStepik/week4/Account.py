class Value:
    def __init__(self):
        self.__val = 0
    def __get__(self, obj, obj_type):
        return self.__val
    def __set__(self, instance, value):
        self.__val = (1-instance.comission)*value

# class Account:
#     amount = Value()
#     def __init__(self, comission):
#         self.comission = comission
#
# if __name__ == '__main__':
#     ac = Account(0.1)
#     ac.amount = 100
#     print(ac.amount)