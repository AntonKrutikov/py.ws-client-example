import asyncio
import json
import websockets
import re

def decode_message(msg:str):
    inner = re.match("a\[(.+)\]", msg)
    return json.loads(inner.group(1))

async def client():
    uri = "wss://stream256.forexpros.com/echo/234/_auw9v6y/websocket"

    async def heartbeat(ws):
        event = json.dumps({"_event":"heartbeat","data":"h"})
        while True:
            await asyncio.sleep(5)
            await websocket.send(json.dumps(event))

    async with websockets.connect(uri) as websocket:
        asyncio.get_event_loop_policy().get_event_loop().create_task(heartbeat(websocket))
        async for message in websocket:
            if message == 'o':
                event = [json.dumps({"_event": "bulk-subscribe", "tzID":18, "message":"pid-eu-1057391:%%pid-eu-1061443:%%pid-eu-1061453:%%pid-eu-1061448:%%pid-eu-1114630:%%pid-eu-13665:%%pid-eu-13666:%%pid-eu-13667:%%pid-eu-13676:%%pid-eu-13673:%%pid-eu-13675:%%pid-eu-169:%%pid-eu-166:%%pid-eu-172:%%pid-eu-179:%%pid-eu-171:%%pid-eu-40820:%%pid-eu-2186:%%pid-eu-1691:%%pid-eu-1:%%pid-eu-8833:%%pid-eu-8849:%%pid-eu-8830:%%pid-eu-8836:%%pid-eu-2:%%pid-eu-3:%%pid-eu-5:%%pid-eu-9:%%pid-eu-1010801:%%pid-eu-27:%%pid-eu-175:%%pid-eu-178:%%pid-eu-8910:%%pid-eu-8883:%%pid-eu-8862:%%pid-eu-2090:%%event-eu-448369:%%event-eu-448367:%%event-eu-448366:%%event-eu-448365:%%event-eu-448364:%%event-eu-448363:%%event-eu-448362:%%isOpenPair-8833:%%isOpenPair-8849:%%isOpenPair-8830:%%isOpenPair-8836:%%isOpenPair-8910:%%isOpenPair-8883:%%isOpenPair-8862:%%domain-7:"})]
                await websocket.send(json.dumps(event))
            if message.startswith('a['):
                print(decode_message(message))


asyncio.get_event_loop_policy().get_event_loop().run_until_complete(client())