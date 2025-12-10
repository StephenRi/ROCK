from typing import Literal

from pydantic import BaseModel


class AgentConfig(BaseModel):
    agent_type: Literal["iflow-cli", "swe-agent"]
    version: str
