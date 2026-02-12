import threading
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from services.telemetry_service import telemetry_service
from mqtt_client import start_mqtt

app = FastAPI()

@app.on_event("startup")
def startup_event():
    thread = threading.Thread(target=start_mqtt, daemon=True)
    thread.start()

@app.websocket("/ws/telemetry")
async def telemetry_ws(ws: WebSocket):
    await ws.accept()
    await telemetry_service.connect(ws)
    try:
        while True:
            await ws.receive_text()
    except WebSocketDisconnect:
        telemetry_service.disconnect(ws)
