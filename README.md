# Back-End Practice: Coin Flip Service with Python and FastAPI

This is an exercise to showcase:

* [Python][1] as a back-end language.

* The basic routing, request-response, and validation features of the
[FastAPI][0] framework.

## Task

* Create a service at the `/rng/coin` endpoint that will generate the "heads"
or "tails" string at random, and serve it as JSON.

* Create a service at the `/rng/coin/:flips` endpoint that will generate
multiple "head" or "tails" strings at random, and serve them as JSON.

* The number of flips is specified as path parameter, and must be an integer
greater than one but no larger than 100.

* Apply type validation and constraint validation. Respond with a 400-family
code to handle invalid values.

* Root should display an html message that directs the user to either the API
documentation or the coin flip service.

## Example URL - Response

### One Valid Coin Flip

```text
/rng/coin
```

```text
HTTP/1.1 200 OK
content-length: 21
content-type: application/json
date: Fri, 09 Feb 2024 08:27:07 GMT
server: uvicorn
```

```json
{
    "coin-flip": "tails"
}
```

### Valid Number of Coin Flips

```text
/rng/coin/5
```

```text
HTTP/1.1 200 OK
content-length: 56
content-type: application/json
date: Fri, 09 Feb 2024 08:42:21 GMT
server: uvicorn
```

```json
{
    "coin-flips": [
        "heads",
        "tails",
        "heads",
        "heads",
        "tails"
    ]
}
```

### Invalid Number of Coin Flips

```text
/rng/coin/101
```

```text
HTTP/1.1 422 Unprocessable Entity
content-length: 177
content-type: application/json
date: Fri, 09 Feb 2024 08:45:44 GMT
server: uvicorn
```

```json
{
    "detail": [
        {
            "ctx": {
                "lt": 101
            },
            "input": "101",
            "loc": [
                "path",
                "flips"
            ],
            "msg": "Input should be less than 101",
            "type": "less_than",
            "url": "https://errors.pydantic.dev/2.6/v/less_than"
        }
    ]
}
```

### Invalid Type for Coin Flips

```text
/rng/coin/red
```

```text
HTTP/1.1 422 Unprocessable Entity
content-length: 204
content-type: application/json
date: Fri, 09 Feb 2024 08:48:14 GMT
server: uvicorn
```

```json
{
    "detail": [
        {
            "input": "red",
            "loc": [
                "path",
                "flips"
            ],
            "msg": "Input should be a valid integer, unable to parse string as an integer",
            "type": "int_parsing",
            "url": "https://errors.pydantic.dev/2.6/v/int_parsing"
        }
    ]
}
```

## Installation

First make sure you already have both [Python][2] and [pip][3]. Then you can
use pip to install the dependencies. The only core dependencies are `fastapi`
and `uvicorn`:

```bash
python -m pip install fastapi uvicorn
```

Or you can install directly from the requirements file, which will also install
type checkers and linters:

```bash
python -m pip install -r requirements.txt
```

## Usage

Once everything is installed, you can run the server using:

```bash
uvicorn main:app
```

## Notes

In FastAPI:
 * HTTP verbs aka HTTP methods are known as *operations*.
 * Handlers are known as *path operation functions*.
 * Variable parts of a path are known as *path parameters*.

Decorators are used to link together *operation*, *path*, and *path
operation function*.

Routing uses the general pattern:

```text
@<FastAPI instance>.<operation>(<path>)
<path operation function>
```

The whole line `@<FastAPI instance>.<operation>(<path>)` is known as *path
operation decorator*, and decorates the *path operation function*, which
is assigned to that specific *operation* and *path*.

*Path parameters* are declared in the *path* between `{}` and also declared
as parameters to the *path operation function*.

Example:

```Python
@app.get("/somepath/{num}")
def get_user_idn(num: int):
    return {"path parameter": num}
```

---

[0]: https://fastapi.tiangolo.com/
[1]: https://www.python.org/
[2]: https://www.python.org/downloads/
[3]: https://pip.pypa.io/en/stable/installation/
