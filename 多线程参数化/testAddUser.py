from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
 #1.开户
from Bank import bank_addUser
#username, password, country, province, street, door, money
da = [
    ["jason","123456","cn","安徽省","桃源路","s001",6000,1],#99
    ["jaso","123456","cn","安徽省","桃源路","s001",6000,1],#100
    ["jason","123456","cn","安徽省","桃源路","s001",6000,2],#重复
    ["jas","123456","cn","安徽省","桃源路","s001",6000,3]#101，已满
]
@ddt
class kh(TestCase):
        for i in range(93):
            name="jason"+str(i)
            bank_addUser(name,"123456","cn","安徽省","桃源路","s001",6000)
        @data(*da)
        @unpack
        def testAddUser(self,a,b,c,d,e,f,g,h):
            result = bank_addUser(a,b,c,d,e,f,g)
            self.assertEqual(result,h)