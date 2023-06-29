from fastapi import Depends, FastAPI
from auth.verify_token import get_query_token

import routers.s3_objects_router as s3_objects_router
import routers.users_router as users_router
import routers.user_objects_router as user_objects_router

import uvicorn

PORT = 8000

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(s3_objects_router.router)
app.include_router(users_router.router)
app.include_router(user_objects_router.router)

@app.get('/')
async def root():
    return {'message': 'Welcome to Hyper Wasabi!'}

if __name__ == '__main__':
    uvicorn.run('main:app', port=PORT, reload=True)