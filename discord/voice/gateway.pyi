from ..state import ConnectionState as ConnectionState
from typing import Any

class VoiceGateway:
    state: Any
    ws: Any
    server_id: Any
    session_id: Any
    secret_key: Any
    def __init__(self, ws, state: ConnectionState, guild_id: int, hook) -> None: ...
    async def hook(self, *args) -> None: ...
    def update_session_id(self, id: int): ...
    async def send_json(self, payload: dict): ...
    async def resume(self) -> None: ...
    async def identify(self) -> None: ...
    gateway: Any
    client: Any
    @classmethod
    async def voice_client_entry(cls, client, *, resume: bool = ..., hook: Any | None = ...): ...
    async def select_protocol(self, ip, port, mode) -> None: ...
    async def client_connect(self) -> None: ...
    async def speak(self, state: int = ...) -> None: ...
    async def recv(self) -> None: ...
    async def heartbeat(self, interval: float): ...
    async def ready(self, data: dict): ...
    async def hello(self, interval: float): ...
    async def close(self, code: int): ...
