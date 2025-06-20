# **Install Strands Agents SDK and tools** 
# pip install strands-agents strands-agents-tools 
# or
# uv init . 
# uv add strands-agents strands-agents-tools
# **Install the required dependency**
# pip install 'strands-agents[anthropic]' or # uv add strands-agents[anthropic]
# uv run Strands_RAG.py

import os
import logging
from strands import Agent
from strands.models.anthropic import AnthropicModel
from strands_tools import current_time, http_request, use_aws, retrieve

# Create agent with Claude 4 from Bedrock
agent = Agent(
    #model=model,
    #tools=[current_time,use_aws]
    tools=[current_time, use_aws, retrieve],
    system_prompt="You are a RAG specialist. Use the retrieve tool for queries. When using the retrieve tool, use all knowledge bases in ap-south-1 in my aws account"
    #system_prompt="You are a RAG specialist. Use the retrieve tool for queries. When using the retrieve tool, always use knowledgeBaseId='' and region='ap-south-1'."
)

response = agent("what do you know about hypertension?")
print(response)
