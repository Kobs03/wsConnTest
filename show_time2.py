#!/usr/bin/env python

import asyncio
import datetime
import random
import websockets
import websockets.server

CONNECTIONS = set()

class MyPolicy(websockets.server.WebSocketServerProtocol):
    async def process_request(self, path, request_headers):
        origin = request_headers.get("Origin", None)
        # Allow connections from any origin
        if origin:
            self.allowed_origin = origin

async def register(websocket):
    CONNECTIONS.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        CONNECTIONS.remove(websocket)

async def show_time():
    
    while True:
        message = datetime.datetime.now(datetime.timezone.utc).isoformat() + "Z"
        random_number = random.randint(1, 100)
        websockets.broadcast(CONNECTIONS, str(random_number))
        await asyncio.sleep(random.random() * 2 + 1)

async def main():
    async with websockets.serve(register, "0.0.0.0", 5678, create_protocol=MyPolicy):
        await show_time()

if __name__ == "__main__":
    asyncio.run(main())