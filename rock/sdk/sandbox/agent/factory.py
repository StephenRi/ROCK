from rock.actions.sandbox.base import AbstractSandbox
from rock.sdk.sandbox.agent.base import Agent
from rock.sdk.sandbox.agent.config import AgentConfig
from rock.sdk.sandbox.agent.iflow_cli import IFlowCli, IFlowCliConfig
from rock.sdk.sandbox.agent.swe_agent import SweAgent, SweAgentConfig


class AgentFactory:
    @staticmethod
    async def create(sandbox: AbstractSandbox, config: AgentConfig) -> Agent:
        if config.agent_type == "iflow-cli":
            assert isinstance(config, IFlowCliConfig)
            agent = IFlowCli(sandbox, config)
            return agent
        elif config.agent_type == "swe":
            assert isinstance(config, SweAgentConfig)
            agent = SweAgent(sandbox, config)
            return agent
        else:
            raise ValueError(f"Unsupported agent type: {config.agent_type}")
