import pytest
from test_unitys.test_yaml_unitys import test_Yaml_unity
import logging
import os
num=10

class Test_long():

    # def test_001_login(self,ceshi_fixture):
    #     print("哦吼")
    #     # logging.basicConfig(filename="debug.log",level=logging.DEBUG)
    #     # os.chdir('./')
    #     # logging.info("开始测试")
    # def number(self):
    #     return 10
    #
    # @pytest.mark.parametrize("x",[(1),('2'),('s')])
    # def test_002_datatest(self,x):
    #     """参数化测试"""
    #     print(x)
    #
    #
    # @pytest.mark.run(order=1)
    # def test_kongzhi_xunshu(self):
    #     print("控制执行循序")
    #
    #
    # @pytest.mark.run(order=1)
    # def test__xunshu(self):
    #     print("控制执行循序两个order=1")
    #
    #
    #
    # @pytest.mark.skip(reason="无条件跳过测试用力")
    # def test_skip_noif(self):
    #     print("测试无条件跳过测试用例")
    #
    # @pytest.mark.skipif(num>1,reason="满足条件跳过测试用例")
    # def test_if_skip(self):
    #     print("满足条件跳过")
    #
    # @pytest.mark.skipif(num<1,reason="不满足条件，需要执行用力")
    # def test_noif_skip(self):
    #     print("不满足条件执行")

    @pytest.mark.parametrize('buzhidao', test_Yaml_unity.read_yaml('test_unitys/data.yaml', 'login'))
    def test_parms_ceshi(self,buzhidao ):
        print(buzhidao)

