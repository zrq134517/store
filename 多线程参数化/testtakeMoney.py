from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
#3.取钱

from Bank import bank_takeMoney

da_qq = [["00000000","123456",-1,3],#-1
         ["00000000","123456",0,0],#0
         ["00000000","123456",1,0],#1
         ["11111111","123456",599,0],#599
         ["22222222","123456",600,0],#600
         ["33333333","123456",601,3],#601
         ["00000001","123456",1,1],#账号不对
         ["00000000","123",1,2],#密码不对
         ["00000001","123",1,1],#账号密码不对
         ["","123456",1,1],#账号空
         ["00000000","",1,2],#密码空
         ["","",1,1],#账号密码空
]
@ddt
class qq(TestCase):
    @data(*da_qq)
    @unpack
    def testtakeMoney(self,a,b,c,d):
        result = bank_takeMoney(a,b,c)
        self.assertEqual(result,d)