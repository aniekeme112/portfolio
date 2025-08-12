import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ProjectConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("projects", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("projects", self.channel_name)

    async def receive(self, text_data):
        # You can optionally handle messages from frontend
        pass

    async def project_update(self, event):
        await self.send(text_data=json.dumps(event["data"]))
