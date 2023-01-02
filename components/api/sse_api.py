from fastapi import APIRouter, Request
from sse_starlette.sse import EventSourceResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import asyncio
import json

router = APIRouter(prefix="/sse/api/v1", tags=["SSE_API "])


async def data_generator():
    count = 0
    done = 10
    # yield {'data': {'status': 'PENDING'}}
    # await asyncio.sleep(10)

    # yield {'data': {'status': 'IN TRANSIT'}}
    # await asyncio.sleep(10)

    # await asyncio.sleep(10)

    while True:

        if count == done:
            JSONResponse(content=jsonable_encoder(
                {'data': {'status': 'FINISHED'}}))
            break
        else:
            print('count----------->', count)
            JSONResponse(content=jsonable_encoder(
                {'data': {'status': 'PENDING'}}))
            count += 1
            await asyncio.sleep(1)


@router.get("/stream")
async def server_events():
    return EventSourceResponse(data_generator())
# async def message_stream(request: Request):
#     def new_messages():
#         yield 'Hello World'

#     async def event_generator():
#         while True:
#             if await request.is_disconnected():
#                 print('AAA')
#                 break

#             if new_messages():
#                 print('BBB')
#                 yield {
#                     'event': 'new_message',
#                     'id': 'message_id',
#                     'retry': RETRY_TIMEOUT,
#                     'data': 'message_content'
#                 }

#             await asyncio.sleep(STREAM_DELAY)
#         print('CCC')
#     print("DDD")
#     return EventSourceResponse(event_generator())
# # @router.get("/realtime-price")
# # def getRealtimePrice():
