from requests import get
import os


def grab_input(link: str, session_cookie: str = None) -> None:
    if session_cookie is None:
        session_cookie = os.getenv("AOC_SESSION")

    if not session_cookie:
        raise ValueError(
            "Session cookie required. Pass it as argument or set AOC_SESSION environment variable"
        )

    headers = {
        "Cookie": f"session={session_cookie}",
        "User-Agent": "github.com/brodycritchlow/adventofcode",
    }

    res = get(link, headers=headers)
    res.raise_for_status()

    with open("input.txt", "w+") as file:
        file.write(res.text)
