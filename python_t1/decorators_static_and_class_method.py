# Class method are methods that can access to the class state, but not
# the instance object state. Then, we can use them without instantiate
# an object


class MyClass:
    """Example class for class method and static method decorators"""

    power = 2

    @classmethod
    def class_method_power_2(
        cls, num
    ):  # We pass cls that is the class state instead of the self instance
        """Return the power 2 of the passed number"""
        return num**cls.power

    # static methods in the other hand don't have access to the class or instance state
    # they are just methods/ functions that belong to the same namespace

    @staticmethod
    def power_two(number):
        """Take a number to the power 2, it does not need to access the class state/scope"""
        return number**2


# Then, to use these methods we do not need to instantiate an object of this class
print(MyClass.class_method_power_2(10))
# the class information is passed as the first argument in this dot notation

print(MyClass.power_two(5))  # this is like calling a function within a namespace
