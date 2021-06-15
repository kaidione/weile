# 分析一个水杯的属性和功能，使用类描述并创建对象
class Cup:
    height = 0
    bulk = 0
    color = ""
    made = ""

    def liquid_story(self):
        print("可以存放", self.bulk, "的液体")


# 笔记本电脑
class Computer:
    scree_size = 0
    price = 0
    cpu_model = ""
    memory = 0
    wait_sleep_time = 0

    def play_keywords(self):
        print("可以打数不清的字")

    def play_games(self):
        print("可以打很多游戏")

    def look_vidio(self):
        print("可以看很多视频")


# 定义一个空调类和对应的测试类
class Air:
    __brand = ""
    __price = 0

    def set_brand(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def action(self):
        print("空调开机了……")

    def shutdown(self, time):
        print("空调将在", time, "分钟后自动关闭")


air = Air()
air.set_brand("格力")
air.set_price(10000)
a = air.get_brand()
print(a)
b = air.get_price()
print(b)
air.action()
air.shutdown(3)


# 定义一个学生类和对应的测试类
class Student:
    __name = ""
    __age = 0

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def introduce(self):
        print("大家好，我叫", self.__name, ",今年", self.__age, "岁了")

    def compare(self, student):
        if self.__age > student.get_age():
            print("我比同桌大", self.__age - student.get_age(), "岁")
        elif self.__age < student.get_age():
            print("我比同桌小", student.get_age() - self.__age)
        else:
            print("我和同桌一样大")


student1 = Student()
student2 = Student()
student1.set_name("温文")
student1.set_age(23)
student2.set_name("龙龙")
student2.set_age(21)
student1.introduce()
student1.compare(student2)


# 打电话业务逻辑
class Human:
    name = ""
    sex = ""
    age = ""
    phone_bill = 0
    phone_brand = ""
    phone_charge_bulk = 0
    scree_size = 0.0
    wait_sleep_time = 0
    integral = 0

    def note(self, text, phone):
        print("将", text, "发送给手机号为", phone, "的用户")

    def call(self, phone, long_time):
        # print(type(int(long_time)))
        if long_time * 10 // 10 != long_time:
            # print(1)
            if phone != "" and self.phone_bill > 1:
                # print(long_time * 10 // 10 + 1)
                if 0 < (long_time * 10 // 10 + 1) <= 10:
                    self.phone_bill = self.phone_bill - (long_time * 10 // 10 + 1) * 1
                    self.integral = self.integral + ((long_time * 10 // 10 + 1) * 15)
                    # print(self.phone_bill)
                    return (long_time * 10 // 10 + 1) * 1
                elif 10 < (long_time * 10 // 10 + 1) <= 20:
                    self.phone_bill = self.phone_bill - (((long_time * 10 // 10 + 1 - 10) * 0.8) + 10 * 1)
                    self.integral = self.integral + (((long_time * 10 // 10 + 1 - 10) * 39) + 10 * 15)
                    return ((long_time * 10 // 10 - 10) * 0.8) + 10 * 1
                elif (long_time * 10 // 10 + 1) > 20:
                    self.phone_bill = self.phone_bill - (((long_time * 10 // 10 + 1 - 20) * 0.65) + 10 * 0.8 + 10 * 0.1)
                    self.integral = self.integral + (((long_time * 10 // 10 + 1 - 20) * 48) + 10 * 39 + 10 * 15)
                    return ((long_time * 10 // 10 - 20) * 0.65) + 10 * 0.8 + 10 * 0.1
            else:
                print("电话不能为空或花费余额不足")
        else:
            # print(0)
            print(self.phone_bill)
            if phone != "" and self.phone_bill > 1:
                # print(long_time * 10 // 10 + 1)
                # print(4)
                print(type(long_time))
                if 0 < long_time <= 10:
                    # print(1)
                    self.phone_bill = self.phone_bill - long_time * 1
                    self.integral = self.integral + long_time * 15
                    # print(self.phone_bill)
                    return long_time * 1
                elif 10 < long_time <= 20:
                    # print(2)
                    self.phone_bill = self.phone_bill - (((long_time - 10) * 0.8) + 10 * 1)
                    self.integral = self.integral + (((long_time - 10) * 39) + 10 * 15)
                    return ((long_time - 10) * 0.8) + 10 * 1
                elif long_time > 20:
                    # print(3)
                    self.phone_bill = self.phone_bill - (((long_time - 20) * 0.65) + 10 * 0.8 + 10 * 0.1)
                    self.integral = self.integral + (((long_time - 20) * 48) + 10 * 39 + 10 * 15)
                    return ((long_time - 20) * 0.65) + 10 * 0.8 + 10 * 0.1
            else:
                print("电话不能为空或花费余额不足")


human1 = Human()
human2 = Human()
human1.phone_bill = 20
human1.note("一起俩看流星雨", "12306")
a = human1.call("12306", 2.1)

print(a)
print(human1.integral)


# print(type(10))


# 定义一个学生类
class Student1:
    stu_number = ""
    stu_name = ""
    stu_age = 0
    stu_sex = ""
    stu_height = 0
    stu_weight = 0
    stu_goal = 0
    stu_address = ""
    stu_phone = ""

    def study(self, hour):
        print(self.stu_name, "已经学习了", hour, "个小时了")

    def play_games(self, game_name):
        print("我玩的游戏的名字是", game_name)

    def programing(self, row_num):
        print("我已经写了", row_num, "的代码了")

    def sum(self, *num):
        sum1 = 0
        # print(num)
        for i in num:
            # print(i)
            sum1 = sum1 + i
        return sum1


student4 = Student1()
print(student4.sum(1, 3, 5, 3, 6, 3))


# 车类
class Car:
    car_name = ""
    car_num = ""
    car_wheels = 0
    car_color = ""
    car_weight = 0
    car_boil_bulk = 0

    def run(self, function):
        print("我最适合的就是", function)


car1 = Car()
car1.car_name = "法拉利"
car1.car_num = "大"
car1.car_wheels = 5
car1.car_color = "红色"
car1.car_weight = 1000
car1.car_boil_bulk = 500
car1.run("越野")
car2 = Car()
car1.car_name = "宝马"
car1.car_num = "大"
car1.car_wheels = 5
car1.car_color = "红色"
car1.car_weight = 1000
car1.car_boil_bulk = 500
car1.run("赛车")
car1 = Car()
car1.car_name = "铃木"
car1.car_num = "大"
car1.car_wheels = 5
car1.car_color = "红色"
car1.car_weight = 1000
car1.car_boil_bulk = 500
car1.run("越野")
car1 = Car()
car1.car_name = "五菱"
car1.car_num = "大"
car1.car_wheels = 5
car1.car_color = "红色"
car1.car_weight = 1000
car1.car_boil_bulk = 500
car1.run("赛车")
car1 = Car()
car1.car_name = "拖拉机"
car1.car_num = "大"
car1.car_wheels = 5
car1.car_color = "红色"
car1.car_weight = 1000
car1.car_boil_bulk = 500
car1.run("越野")
car1 = Car()

# 笔记本
class Notebook:
    notebook_num = ""
    wait_time = 0
    note_color = ""
    note_weight = 0
    note_cpu = ""
    note_memory_size = 0
    hard_disk_size = 0

    def play_game(self, game_name):
        print("我玩了", game_name, "9个小时了")

    def work(self):
        print("我已经工作3个小时了")

# 猴子
class Monkey:
    monkey_num = ""
    monkey_sex = ""
    body_color = ""
    monkey_weight = 0

    def make_fire(self,meterial):
        print("猴子用", meterial, "来生火")

    def study_thing(self,*thing):
        print("猴子可以学习的有", thing)


