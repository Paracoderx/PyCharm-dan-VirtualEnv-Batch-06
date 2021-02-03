import requests
print("helo world")
try:
    r = requests.get('https://goog e.com')
    print(r.status_code)
    if r.status_code == 200:
        print(r.text)
except Exception as e:
    print("ada errorrrr", e)

