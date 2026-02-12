class TelemetryService:
    def __init__(self):
        self.clients = set()

    async def connect(self, websocket):
        self.clients.add(websocket)

    def disconnect(self, websocket):
        self.clients.remove(websocket)

    async def broadcast(self, data: str):
        for client in self.clients:
            await client.send_text(data)

telemetry_service = TelemetryService()
