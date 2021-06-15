# 定义老手机类
class Oldphone:
    __brand = ""

    def __init__(self, brand):
        self.__brand = brand

    def setbrand(self, brand):
        self.__brand = brand

    def getbrand(self):
        return self.__brand

    def call(self, phone):
        print("正在给", phone, "打电话")


class Newphone(Oldphone):
    def call(self, phone):
        print("语音拨号中……")
        super().call(phone)

    def introduce(self):
        print("品牌为：", self.getbrand(), "的手机很好用")


phone = Newphone("华为")
print(phone.getbrand())
phone.setbrand("小米")
print(phone.getbrand())
phone.introduce()
phone.call("10086")


# 厨师类
class Cook:
    __name = ""
    __age = ""

    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name

    def setage(self, age):
        self.__age = age

    def getage(self):
        return self.__age

    def steam_rice(self):
        print("这是一个蒸饭方法")


class big_cook(Cook):
    def cooking(self):
        print("这是一个炒菜的方法")


class small_cook(big_cook):
    def steam_rice_cooking(self):
        super().steam_rice()
        super().cooking()


scok = small_cook()
scok.setname("张三")
scok.setage(30)
print(scok.getname())
print(scok.getage())
scok.steam_rice()
scok.cooking()
scok.steam_rice_cooking()


# 人类
class Person:
    age = 0
    sex = ""
    name = ""

    def work(self):
        print("我可以做很多工作")

    def study(self):
        print("学习永无止境")

    def sing(self):
        print("唱歌使人快乐")


class Worker(Person):
    def work(self):
        super().work()


class Students(Person):
    stu_num = ""

    def study(self):
        super().study()

    def sing(self):
        super().sing()


