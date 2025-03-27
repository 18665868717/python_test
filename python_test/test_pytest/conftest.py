import pytest
@pytest.fixture(scope='class')
def my_class_fixture():
    print('测试类前置方法')
    yield
    print('测试类后置方法')

@pytest.fixture(scope='function')
def my_function_fixture():
    print('测试函数前置方法')
    # yield
    # print('测试函数后置方法')

@pytest.fixture(scope='module',autouse=True)
def my_module_fixture():
    print('测试模块前置方法')
    yield
    print('测试模块后置方法')

@pytest.fixture(scope='session',autouse=True)
def my_session_fixture():
    print('测试session前置方法')
    yield
    print('测试session置方法')

data=[{"user":"liuyang","password":"还好吗"},
    {"user":"chengsuyu","password":"还好吗"},
      ]
# ids也是要结合着params一起使用的。当有多个 param 时，针对每一个 param，可以指定一个id， 然后，这个
# id会变成测试用例名字的一部分。如果没有提供 id，则id将自动生成。
@pytest.fixture(scope='function',params=data,ids=['data1','data2'])
# @pytest.fixture(scope='function',params=['data1','data2'])
def my_params_fixture(request):
    # print("前置方法")
    yield request.param
    # print("后置方法")