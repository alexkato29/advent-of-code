from pathlib import Path
import tomllib
from dataclasses import dataclass


@dataclass(frozen=True)
class Secrets:
    session_cookie: str


def load_secrets(path: Path | None = None) -> Secrets:
    if not path:
        path = Path(__file__).resolve().parents[1] / "secrets.toml"

    with path.open("rb") as f:
        raw = tomllib.load(f)

    return Secrets(
        session_cookie=raw["aoc"]["session_cookie"],
    )

SECRETS = load_secrets()
