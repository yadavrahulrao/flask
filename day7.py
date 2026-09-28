from fastapi import FastAPI, WebSocket , WebSocketDisconnect

# from pydantic import BaseModel

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket:WebSocket):
    await websocket.accept()
    print("client connected")

    try :
        while True:
            data = await websocket.receive_text()
            print("data recieved")
            await websocket.send_text(f"data send to client:{data}")


    except WebSocketDisconnect :
        print("client disconnected successfully")