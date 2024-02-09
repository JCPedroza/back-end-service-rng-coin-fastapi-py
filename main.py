from typing import Annotated
from random import choice
from fastapi import FastAPI, Path
from fastapi.responses import HTMLResponse

COIN = "heads", "tails"
MIN_FLIPS = 2
MAX_FLIPS = 101
OAPI_PATH = "/docs"
RDOC_PATH = "/redocs"

app = FastAPI(docs_url=OAPI_PATH, redoc_url=RDOC_PATH)


@app.get("/", response_class=HTMLResponse)
def get_root() -> str:
    """Display instructions."""

    return f"""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <title>Root</title>
        </head>
        <body>
            <p>Check the documentation at:<ul>
                <li><a href={OAPI_PATH}>{OAPI_PATH}</a></li>
                <li><a href={RDOC_PATH}>{RDOC_PATH}</a></li>
            </ul></p>
        </body>
    </html>
    """


@app.get("/rng/coin")
def get_rng_coin() -> dict[str, str]:
    """Simulate a coin flip."""
    return {"coin-flip": choice(COIN)}


@app.get("/rng/coin/{flips}")
def get_rng_coin_FLIPS(
    flips: Annotated[int, Path(ge=MIN_FLIPS, lt=MAX_FLIPS)]
) -> dict[str, list[str]]:
    """Simulate multiple coin flips."""
    return {"coin-flips": [choice(COIN) for _ in range(flips)]}
