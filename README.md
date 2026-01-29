# Moss MCP Server

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP](https://img.shields.io/badge/MCP-Protocol-green.svg)](https://modelcontextprotocol.io/)

A Model Context Protocol (MCP) server for managing high-performance semantic search indexes using the [Moss REST API](https://docs.usemoss.dev/api-reference/introduction).

## ✨ Key Features

- **Semantic Index Management**: Create, list, and delete vector indexes optimized for sub-10ms performance.
- **Efficient Document Handling**: Add, update, and remove documents with ease.
- **REST-Based Management**: Full control over your Moss project directly from your AI assistant.
- **Seamless Claude Integration**: Pre-configured for Claude Desktop.

## 🚀 Getting Started

### 1. Prerequisites

- Python 3.10 or higher
- A Moss Project (Sign up at [portal.usemoss.dev](https://portal.usemoss.dev))

### 2. Installation

```bash
pip install fastmcp httpx inferedge-moss python-dotenv
```

### 3. Setup Credentials

1. Go to the [Moss Portal](https://portal.usemoss.dev).
2. Create or select a project.
3. Obtain your `PROJECT_ID` and `PROJECT_KEY` from the project settings.

### 4. Environment Variables

Create a `.env` file in your project directory:

```env
MOSS_PROJECT_ID="your_project_id"
MOSS_PROJECT_KEY="your_project_key"
```

## 🛠️ Tool Reference

The following tools are exposed by the Moss MCP server:

| Tool               | Parameters                             | Description                             |
| ------------------ | -------------------------------------- | --------------------------------------- |
| `create_index`     | `index_name`, `documents`, `model_id?` | Create a new semantic search index.     |
| `get_index`        | `index_name`                           | Retrieve metadata for a specific index. |
| `list_indexes`     | -                                      | List all indexes in the project.        |
| `add_documents`    | `index_name`, `documents`, `upsert?`   | Add or update documents in an index.    |
| `delete_documents` | `index_name`, `doc_ids`                | Remove specific documents by their IDs. |
| `get_documents`    | `index_name`, `doc_ids?`               | Retrieve document content and metadata. |
| `delete_index`     | `index_name`                           | Permanently delete an index.            |

## 💻 Claude Desktop Configuration

Add this to your Claude Desktop configuration file:

- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

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

> [!IMPORTANT]
> Replace `/absolute/path/to/moss_server.py` with the actual path on your machine.

## 📖 Usage Example

Once configured, you can ask Claude to manage your indexes:

**User Prompt:**

> "Create a new Moss index named 'kb-docs' and add these documents detailing our API guidelines: [docs...]"

**User Prompt:**

> "List all my current Moss indexes and tell me how many documents are in each."

## ⚡ Note on Semantic Querying

The Moss REST API handles **index management** (CRUD operations). For **high-speed semantic search queries** (sub-10ms), use the [Moss Python SDK](https://docs.usemoss.dev/reference/python/api) directly in your application code.

```python
from moss import MossClient

client = MossClient(project_id="...", project_key="...")
results = client.query(index_name="kb-docs", text="What is the rate limit?")
```

## 🔗 Resources

- [Official Documentation](https://docs.usemoss.dev)
- [Moss Portal](https://portal.usemoss.dev)
- [GitHub Repository](https://github.com/CoderOMaster/moss-mcp)

## 📝 Technical Case Study

- [Building Voice-Native Semantic Search: Moss MCP + Vapi](./VAPI_BLOG.md) — A deep dive into using Streamable HTTP (shttp) to power real-time voice agents with semantic knowledge.

---
