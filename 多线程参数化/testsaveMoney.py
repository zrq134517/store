from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
##2.存钱
from Bank import bank_saveMoney

da_cq = [["00000000",0,True],#0
         ["00000000",1,True],#1
         ["00000000",-1,False],#-1
         ["00000001",1,False],#账号错误
         ["00000000",100000000000000000000,True],#额数大
         ["",1,False]#账号空
]
@ddt
class cq(TestCase):
    @data(*da_cq)
    @unpack
    def testsaveMoney(self,a,b,c):
        result = bank_saveMoney(a,b)
        self.assertEqual(result,c)
