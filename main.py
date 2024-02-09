from typing import Annotated
from random import choice
from fastapi import FastAPI, Path
from fastapi.responses import HTMLResponse

COIN = "heads", "tails"
MIN_TOSSES = 2
MAX_TOSSES = 101
OAPI_PATH = "/docs"
RDOC_PATH = "/redocs"

app = FastAPI(docs_url=OAPI_PATH, redoc_url=RDOC_PATH)


@app.get("/", response_class=HTMLResponse)
def get_root() -> str:
    """Get root instructions."""

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
    """Randomly generate a coin side."""
    return {"coin-side": choice(COIN)}


@app.get("/rng/coin/{tosses}")
def get_rng_coin_TOSSES(
    tosses: Annotated[int, Path(ge=MIN_TOSSES, lt=MAX_TOSSES)]
) -> dict[str, list[str]]:
    """Randomly generate multiple coin sides."""
    return {"coin-sides": [choice(COIN) for _ in range(tosses)]}
