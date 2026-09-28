import asyncio
import websockets

async def echo_handler(websocket):
    print("client is connected")

    try :
        async for message in websocket:
            print(f"recive message from client:{message}")
            response = f"echo:{message}"
            await websocket.send(response)
    except websockets.exceptions.ConnectionClosedOK:
        print("disconnected")

    except Exception as e :
        print(f"error:{e}")


async def main():
    async with websockets.serve(echo_handler,"localhost",8765):
        print("the server is running on the ws://localhost:8765")
        await asyncio.Future()


if __name__ == "__main__" :
    asyncio.run(main())


            