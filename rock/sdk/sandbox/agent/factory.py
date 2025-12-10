from rock.actions.sandbox.base import AbstractSandbox
from rock.sdk.sandbox.agent.base import Agent
from rock.sdk.sandbox.agent.config import AgentConfig
from rock.sdk.sandbox.agent.iflow_cli import IFlowCli, IFlowCliConfig
from rock.sdk.sandbox.agent.swe_agent import SweAgent, SweAgentConfig


class AgentFactory:
    @staticmethod
    async def create(sandbox: AbstractSandbox, config: AgentConfig) -> Agent:
        match config.agent_type:
            case "iflow-cli":
                assert isinstance(config, IFlowCliConfig)
                agent = IFlowCli(sandbox, config)
                return agent
            case "swe-agent":
                assert isinstance(config, SweAgentConfig)
                agent = SweAgent(sandbox, config)
                return agent
