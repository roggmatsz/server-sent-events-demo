import asyncio
import itertools
import zlib
from starlette.applications import Starlette
from starlette.responses import StreamingResponse
import data

app = Starlette()

@app.route('/sse{id:int}')
async def sse_endpoint(req):
   return StreamingResponse(
      sse_generator(req),
      headers={
         "Content-type": "text/event-stream",
         "Cache-Control": "no-cache",
         "Connection": "keep-alive",
         "Content-Encoding": "deflate"
      }
   )

async def sse_generator(req):
   id = req.path_params['id']
   stream = zlib.compressobj()
   for i in itertools.count():
      result = data.get(id, i)
      result = b'id: %d\ndata: %d\n\n' % (i, data)
      yield stream.compress(result)
      yield stream.flush(zlib.Z_SYNC_FLUSH)
      await asyncio.sleep(1)