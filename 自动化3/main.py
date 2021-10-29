from HTMLTestRunner import HTMLTestRunner
import unittest
from threading import Thread
import os
class icbc(Thread):
    pettern = ""
    description = ""
    file = ""
    def run(self) -> None:
        # 加载所有用例
        tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern=self.pettern)
        # 执行器
        runner = HTMLTestRunner.HTMLTestRunner(
            title="HKR系统测试报告",
            description = self.description,
            verbosity = 1,
            stream = open(file=self.file, mode="w+", encoding="utf-8")
        )
        runner.run(tests)

att1=icbc()
att1.pettern="Test1.py"
att1.description="HKR系统成功登陆测试"
att1.file="hkr1.html"
att1.start()
att2=icbc()
att2.pettern="Test2.py"
att2.description="HKR系统失败登陆测试"
att2.file="hkr2.html"
att2.start()


