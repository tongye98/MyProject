class MyClass:
    def my_method(self):
        print("Hello, world!")

# 创建 MyClass 的实例
obj = MyClass()

# 获取方法对象
method = obj.my_method
print(method)

# 获取与方法对象相关联的函数对象
function = method.__func__
print(str(function))