from unittest import mock

import pytest

from rock.sdk.sandbox.agent.factory import AgentFactory
from rock.sdk.sandbox.agent.iflow_cli import IFlowCli, IFlowCliConfig
from rock.sdk.sandbox.agent.swe_agent import SweAgent, SweAgentConfig
from rock.sdk.sandbox.client import Sandbox


@pytest.mark.asyncio
async def test_factory_create():
    # Test IFlowCli agent creation
    iflow_config = IFlowCliConfig(version="1.0", install_url="http://example.com/iflow")
    sandbox = mock.Mock(spec=Sandbox)
    iflow_agent = await AgentFactory.create(sandbox, iflow_config)
    assert isinstance(iflow_agent, IFlowCli)
    assert iflow_agent.config == iflow_config

    # Test SweAgent creation
    swe_config = SweAgentConfig(version="1.0")
    swe_agent = await AgentFactory.create(sandbox, swe_config)
    assert isinstance(swe_agent, SweAgent)
    assert swe_agent.config == swe_config
