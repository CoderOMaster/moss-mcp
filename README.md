# Moss MCP Server

MCP server for managing Moss indexes using the [Moss REST API](https://docs.usemoss.dev/api-reference/introduction).

## Setup

### 1. Install

```bash
pip install fastmcp httpx inferedge-moss
```

### 2. Get Credentials

1. Sign up at [portal.usemoss.dev](https://portal.usemoss.dev)
2. Copy your `PROJECT_ID` and `PROJECT_KEY`

### 3. Set Environment Variables

```bash
export MOSS_PROJECT_ID="your_project_id"
export MOSS_PROJECT_KEY="your_project_key"
```

## Usage

### Run Server

```bash
python moss_server.py
```

### Configure Claude Desktop

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "moss": {
      "command": "python",
      "args": ["/absolute/path/to/moss_server.py"],
      "env": {
        "MOSS_PROJECT_ID": "your_project_id",
        "MOSS_PROJECT_KEY": "your_project_key"
      }
    }
  }
}
```

Restart Claude Desktop.

### Example

Ask Claude:

```
Create a Moss index called "docs" with these documents:
[
  {"id": "1", "text": "Python is a programming language"},
  {"id": "2", "text": "JavaScript is for web development"}
]
```

## Available Tools

| Tool | Description |
|------|-------------|
| `create_index` | Create a new index with documents |
| `get_index` | Get index metadata |
| `list_indexes` | List all indexes |
| `add_documents` | Add/update documents in an index |
| `delete_documents` | Delete specific documents |
| `get_documents` | Retrieve stored documents |
| `delete_index` | Delete an index |

## Note on Querying

The Moss REST API handles index management but **not semantic search queries**. For querying, you need the [Moss Python SDK](https://docs.usemoss.dev/reference/python/api) which runs queries client-side for sub-10ms performance.

To add query functionality, install `inferedge-moss` and use the SDK's query methods.

## Resources

- [Moss API Docs](https://docs.usemoss.dev/api-reference/introduction)
- [Moss Portal](https://portal.usemoss.dev)
- [Moss Discord](https://discord.gg/eMXExuafBR)
