import websockets
import asyncio
import os
from threading import Thread
from multiprocessing import Process

class CommandsServer:
    def __init__(self):
        self.cmd="nth"
        self.isWork=True
    def change_cmd(self,command: str):
        self.cmd = command
    
    async def echo(self,websocket, path):
        self.isWork = True
        print("websocket recieved")
        while self.isWork:                   
            await asyncio.sleep(0.3)
            self.isWork = self.cmd != "stop"
            if self.cmd != "nth":
                print(self.cmd)
                await websocket.send(self.cmd)
                self.cmd = "nth"
    
    def start_server(self,loop):
        print("Server Started")
        print("Waiting Websockets...")
        server=websockets.serve(self.echo, 'localhost', 8765,loop=loop)
        loop.run_until_complete(server)
        loop.run_forever()
        print("Server Ended")
    def run(self):
        loop = asyncio.new_event_loop()
        t = Thread(target=self.start_server, args=(loop,))
        t.start()
                
