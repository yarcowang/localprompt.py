# localprompt

A Python client library for Prompt Studio API.

## Installation

```bash
pip install localprompt
```

## Usage

```python
from localprompt import LocalPrompt

# Initialize the client
lp = LocalPrompt('http://localhost:30017')

# Get prompt by ID
prompt = lp.get_prompt_by_id(16)
print(prompt['content'])

# Get prompt by slug
prompt = lp.get_prompt_by_slug('agent-product')
print(prompt['content'])

# Get prompt by ID or slug
prompt = lp.get_prompt(16)
prompt = lp.get_prompt('agent-product')
```

## License

MIT
