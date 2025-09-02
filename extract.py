import requests

URL = "https://tv-1.iill.top/m3u/MyTV"
OUTPUT = "MyTV.m3u"

def fetch_m3u():
    try:
        resp = requests.get(URL, timeout=15)
        resp.raise_for_status()
        content = resp.text

        # 保存到文件
        with open(OUTPUT, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✅ 已成功更新 {OUTPUT}，共 {len(content.splitlines())} 行")
    except Exception as e:
        print("❌ 抓取失败:", e)

if __name__ == "__main__":
    fetch_m3u()
