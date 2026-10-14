import requests
import os

def main():
    token = os.environ.get("PUSHPLUS_TOKEN")
    if not token:
        print("错误：没找到环境变量 PUSHPLUS_TOKEN")
        return
    title = "测试通知"
    content = "收到了这条消息，说明 GitHub 和微信的通路完全没问题。"
    url = "http://www.pushplus.plus/send"
    payload = {"token": token, "title": title, "content": content}
    try:
        resp = requests.post(url, json=payload, timeout=10)
        print("发送成功，服务器返回：", resp.text)
    except Exception as e:
        print("发送失败：", e)

if __name__ == "__main__":
    main()
