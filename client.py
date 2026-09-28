import asyncio
import websockets 

async def communicate():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket :
        message = "hello server"
        print(f"sent message to server :{message}")
        await websocket.send(message)

        response = await websocket.recv()
        print(f"the message will be recieve :{response}")


if __name__ == "__main__":
    asyncio.run(communicate())