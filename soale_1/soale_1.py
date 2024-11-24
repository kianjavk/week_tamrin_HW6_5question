import requests
from requests.auth import HTTPBasicAuth

# جایگزینی با توکن دسترسی شخصی خود
ACCESS_TOKEN = input("your github api:")

# آدرس URL API گیت‌هاب برای دریافت اطلاعات کاربر
API_URL = 'https://api.github.com/user'

# ارسال درخواست GET به API گیت‌هاب با استفاده از توکن برای احراز هویت
response = requests.get(API_URL, auth=HTTPBasicAuth('username', ACCESS_TOKEN))

# بررسی موفقیت درخواست
if response.status_code == 200:
    user_data = response.json()
    print(f"کاربر: {user_data['login']}")

    # دریافت مخازن عمومی کاربر
    repos_url = user_data['repos_url']
    repos_response = requests.get(repos_url, auth=HTTPBasicAuth('username', ACCESS_TOKEN))

    if repos_response.status_code == 200:
        repos = repos_response.json()
        print("مخازن عمومی:")
        for repo in repos:
            print(f"نام: {repo['name']}, آدرس: {repo['html_url']}")
    else:
        print(f"دریافت مخازن با خطا مواجه شد: {repos_response.status_code}")
else:
    print(f"دریافت اطلاعات کاربر با خطا مواجه شد: {response.status_code}")


# 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