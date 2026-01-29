"""
Moss MCP Server - Semantic Search for AI Assistants
Uses Moss REST API for index management and Python SDK for querying
"""

import os
import httpx
from typing import List, Dict
from fastmcp import FastMCP
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize MCP server
mcp = FastMCP("Moss")

# Moss API configuration
BASE_URL = "https://service.usemoss.dev"
PROJECT_ID = os.getenv("MOSS_PROJECT_ID")
PROJECT_KEY = os.getenv("MOSS_PROJECT_KEY")


def get_headers():
    """Get required headers for Moss API"""
    if not PROJECT_KEY:
        raise ValueError("MOSS_PROJECT_KEY environment variable must be set")
    return {
        "Content-Type": "application/json",
        "x-project-key": PROJECT_KEY,
        "x-service-version": "v1"
    }


@mcp.tool()
async def create_index(index_name: str, documents: List[Dict[str, str]], model_id: str = "moss-minilm"):
    """
    Create a new semantic search index.
    
    Args:
        index_name: Name for the index
        documents: List of {"id": "...", "text": "...", "metadata": {...}} documents
        model_id: Embedding model (default: moss-minilm)
    """
    if not PROJECT_ID:
        raise ValueError("MOSS_PROJECT_ID environment variable must be set")
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BASE_URL}/manage",
            headers=get_headers(),
            json={
                "action": "createIndex",
                "projectId": PROJECT_ID,
                "indexName": index_name,
                "modelId": model_id,
                "docs": documents
            },
            timeout=30.0
        )
        response.raise_for_status()
        return f"Created index '{index_name}' with {len(documents)} documents"


@mcp.tool()
async def get_index(index_name: str):
    """Get metadata for a specific index"""
    if not PROJECT_ID:
        raise ValueError("MOSS_PROJECT_ID environment variable must be set")
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BASE_URL}/manage",
            headers=get_headers(),
            json={
                "action": "getIndex",
                "projectId": PROJECT_ID,
                "indexName": index_name
            },
            timeout=30.0
        )
        response.raise_for_status()
        return response.json()


@mcp.tool()
async def list_indexes():
    """List all available indexes"""
    if not PROJECT_ID:
        raise ValueError("MOSS_PROJECT_ID environment variable must be set")
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BASE_URL}/manage",
            headers=get_headers(),
            json={
                "action": "listIndexes",
                "projectId": PROJECT_ID
            },
            timeout=30.0
        )
        response.raise_for_status()
        return response.json()


@mcp.tool()
async def add_documents(index_name: str, documents: List[Dict[str, str]], upsert: bool = True):
    """
    Add documents to an existing index.
    
    Args:
        index_name: Name of the index
        documents: List of {"id": "...", "text": "...", "metadata": {...}} documents
        upsert: Update existing documents (default: True)
    """
    if not PROJECT_ID:
        raise ValueError("MOSS_PROJECT_ID environment variable must be set")
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BASE_URL}/manage",
            headers=get_headers(),
            json={
                "action": "addDocs",
                "projectId": PROJECT_ID,
                "indexName": index_name,
                "docs": documents,
                "options": {"upsert": upsert}
            },
            timeout=30.0
        )
        response.raise_for_status()
        result = response.json()
        return f"Added {result.get('added', 0)} documents, updated {result.get('updated', 0)}"


@mcp.tool()
async def delete_documents(index_name: str, doc_ids: List[str]):
    """
    Delete specific documents from an index.
    
    Args:
        index_name: Name of the index
        doc_ids: List of document IDs to delete
    """
    if not PROJECT_ID:
        raise ValueError("MOSS_PROJECT_ID environment variable must be set")
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BASE_URL}/manage",
            headers=get_headers(),
            json={
                "action": "deleteDocs",
                "projectId": PROJECT_ID,
                "indexName": index_name,
                "docIds": doc_ids
            },
            timeout=30.0
        )
        response.raise_for_status()
        result = response.json()
        return f"Deleted {result.get('deleted', 0)} documents"


@mcp.tool()
async def get_documents(index_name: str, doc_ids: List[str] = None):
    """
    Retrieve documents from an index.
    
    Args:
        index_name: Name of the index
        doc_ids: Optional list of specific document IDs to retrieve
    """
    if not PROJECT_ID:
        raise ValueError("MOSS_PROJECT_ID environment variable must be set")
    
    payload = {
        "action": "getDocs",
        "projectId": PROJECT_ID,
        "indexName": index_name
    }
    
    if doc_ids:
        payload["options"] = {"docIds": doc_ids}
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BASE_URL}/manage",
            headers=get_headers(),
            json=payload,
            timeout=30.0
        )
        response.raise_for_status()
        return response.json()


@mcp.tool()
async def delete_index(index_name: str):
    """Delete an index and all its documents"""
    if not PROJECT_ID:
        raise ValueError("MOSS_PROJECT_ID environment variable must be set")
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BASE_URL}/manage",
            headers=get_headers(),
            json={
                "action": "deleteIndex",
                "projectId": PROJECT_ID,
                "indexName": index_name
            },
            timeout=30.0
        )
        response.raise_for_status()
        return f"Deleted index '{index_name}'"


if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8080)
