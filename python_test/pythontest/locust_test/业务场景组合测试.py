import requests
import csv
import time

LOGIN_URL = "http://your-api-host/api/login"  # ✅ 替换为你的登录接口地址
INPUT_FILE = "accounts.csv"
OUTPUT_FILE = "token_pool.txt"
HEADERS = {"Content-Type": "application/json"}

MAX_RETRY = 3
SLEEP_BETWEEN = 0.05  # 防止被封，建议间隔一下


def login_and_get_token(username, password):
    for _ in range(MAX_RETRY):
        try:
            res = requests.post(LOGIN_URL, json={
                "username": username,
                "password": password
            }, headers=HEADERS)

            if res.status_code == 200 and "token" in res.json():
                return res.json()["token"]
        except Exception as e:
            print(f"登录异常：{e}")
        time.sleep(0.5)  # 重试间隔
    return None


def main():
    success_count = 0
    fail_count = 0

    with open(INPUT_FILE, "r") as infile, open(OUTPUT_FILE, "w") as outfile:
        reader = csv.reader(infile)
        for row in reader:
            if len(row) != 2:
                continue
            username, password = row
            token = login_and_get_token(username, password)
            if token:
                outfile.write(token + "\n")
                success_count += 1
            else:
                print(f" 登录失败：{username}")
                fail_count += 1
            time.sleep(SLEEP_BETWEEN)

    print(f" 登录成功：{success_count} 个")
    print(f" 登录失败：{fail_count} 个")


if __name__ == "__main__":
    main()
