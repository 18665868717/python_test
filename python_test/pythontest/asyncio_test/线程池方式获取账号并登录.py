import pandas as pd
import requests

login_url=""

# 从 Excel 文件读取账号信息
def login(account):
    # 模拟 HTTP POST 请求进行登录
    try:
        response = requests.post(login_url, data=data)

        # 判断登录是否成功（根据返回的 HTTP 状态码或响应内容）
        if response.status_code == 200:
            print(f"登录成功: {username}")
        else:
            print(f"登录失败: {username}, 状态码: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"请求错误: {username}, 错误: {e}")
def load_accounts_from_excel(file_path):
    # 读取 Excel 文件
    df = pd.read_excel(file_path)
    print(df)
    # 将 DataFrame 转换为字典列表
    accounts = df.to_dict(orient='records')

    return accounts

def login_with_thread_pool(accounts):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(login, accounts)

# 示例用法
if __name__ == '__main__':

    accounts = load_accounts_from_excel('../locust_test/USER_INFO.xlsx')
    login_with_thread_pool(accounts)
