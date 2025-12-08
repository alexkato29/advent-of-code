from requests import get, Response

from utils.secrets import SECRETS


def get_dummy_input() -> str:
	with open("dummy_input.txt", "r") as f:
		return f.read().strip()


def get_input(year: int, day: int) -> str:
	url: str = f"https://adventofcode.com/{year}/day/{day}/input"
	cookies: dict[str, str] = {
		"session": SECRETS.session_cookie
	}

	r: Response = get(url=url, cookies=cookies)
	return r.text.strip()
