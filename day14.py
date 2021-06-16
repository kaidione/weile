import threading
import time

# 全局变量
from typing import Any, Union

contain = 0

price = 3


# 创建厨师类
class Cooker(threading.Thread):
    cooker_name = ""
    count = 0

    def run(self) -> None:
        global contain
        while True:
            if contain == 500:
                time.sleep(5)
                print(self.cooker_name, "造了", self.count)
                continue
            else:
                contain = contain + 1
                self.count = self.count + 1
                print(self.cooker_name, "造了1个")
                time.sleep(0.5)


# 创建顾客类
class Customer(threading.Thread):
    customer_name = ""
    money = 600
    count = 0

    def run(self) -> None:
        global contain
        global price
        while True:
            if self.money == 0:
                print(self.customer_name, "没钱了，抢到了", self.count)
                break
            else:
                if contain > 0:
                    contain = contain - 1
                    self.money = self.money - price
                    self.count = self.count + 1
                    print(self.customer_name, "抢到了1个")
                    time.sleep(0.5)
                else:
                    time.sleep(3)
                    continue


c1 = Cooker()
c1.cooker_name = "厨师1"
c2 = Cooker()
c2.cooker_name = "厨师2"
c3 = Cooker()
c3.cooker_name = "厨师3"


cu1 = Customer()
cu1.customer_name = "顾客1"
cu2 = Customer()
cu2.customer_name = "顾客2"
cu3 = Customer()
cu3.customer_name = "顾客3"
cu4 = Customer()
cu4.customer_name = "顾客4"
cu5 = Customer()
cu5.customer_name = "顾客5"
cu6 = Customer()
cu6.customer_name = "顾客6"
# print(cu3.money)
c1.start()
c2.start()
c3.start()

cu1.start()
cu2.start()
cu3.start()
