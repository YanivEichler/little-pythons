from fake_useragent import UserAgent
from http import HTTPStatus
import requests


def get_user_agent() -> str:
    ua = UserAgent()
    return ua.chrome


def get_status_desc(status_code: int) -> str:
    for value in HTTPStatus:
        if value == status_code:
            description: str = f"({value} {value.name}) {value.description}"
            return description
    return "(???) Unknown status code..."


def check_website(website: str, user_agent):
    try:
        code: int = requests.get(website, headers={'User-Agent': user_agent}).status_code
        print(website, get_status_desc(code))
    except Exception:
        print(f"**Couldn't get info for website: \"{website}\"")


def main():
    user_agent: str = get_user_agent()
    while True:
        site: str = input("Please enter an HTTPS URL or type 'quit': ")
        if site.lower() == 'quit':
            break
        check_website(site, user_agent)


if __name__ == '__main__':
    main()
