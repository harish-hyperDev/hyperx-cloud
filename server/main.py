from fastapi import Depends, FastAPI
from auth.verify_token import get_query_token

import routers.s3_router as s3_router
import routers.users as users

import uvicorn

PORT = 8000

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(s3_router.router)
app.include_router(users.router)

@app.get('/')
async def root():
    return {'message': 'Hello World!'}

if __name__ == '__main__':
    uvicorn.run('main:app', port=PORT, reload=True)