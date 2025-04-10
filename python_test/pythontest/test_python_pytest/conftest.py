import pytest

@pytest.fixture(scope='class')
def ceshi_fixture():
    print("开始执行fix")
    yield
    print("结束执行fix")

# @pytest.fixture(scope="function",autouse=False,params=["第一个参数","第二个参数"])
# def parmas_test():
#     print("第一个参数")
#     yield request.param
#     print("最后一个参数")