from fastapi import Header, HTTPException
from typing_extensions import Annotated

import helpers.config as Config


async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != Config.AUTH_TOKEN:
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(query: Annotated[str, Header()]):
    # return {'messsage': 'got query token'}
    if query != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")