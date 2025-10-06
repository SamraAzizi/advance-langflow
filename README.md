# Advance LangFlow Web 🌐

A streamlined web interface for advanced LangFlow operations, providing enhanced workflow management and AI pipeline capabilities.

## 📋 Project Overview

This project offers a web-based interface for managing and executing advanced LangFlow workflows with simplified operations and improved user experience.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- UV package manager (recommended) or pip

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/SamraAzizi/advance-langflow.git
cd advance-langflow
```

2. **Install dependencies using UV**

```bash
uv sync
```

3. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. **Run the application**

```bash
python main.py
```

### Alternative Installation with pip

```bash
pip install -r requirements.txt
python main.py
```

### Project Structure

```bash

advance-langflow/
├── main.py                 # Main application entry point
├── web_operations.py       # Web interface operations and handlers
├── snapshot_operations.py  # Workflow snapshot management
├── prompts.py             # Prompt templates and management
├── pyproject.toml         # Project dependencies and configuration
├── uv.lock                # Lock file for dependency versions
├── .env                   # Environment variables (create from .env.example)
├── .gitignore            # Git ignore rules
└── .python-version       # Python version specification
```

## Configuration
### Environment Variables

Create a .env file with the following variables:

```bash
# API Keys
OPENAI_API_KEY=your_openai_api_key_here
LANGSMITH_API_KEY=your_langsmith_key
LANGSMITH_PROJECT=advance-langflow

# Application Settings
HOST=localhost
PORT=7860
DEBUG=True

# Database (if applicable)
DATABASE_URL=sqlite:///./langflow.db
```

## Usage

### Starting the Web Interface
```bash
python main.py
```

The application will start and be accessible at `http://localhost:7860`

### Key Features

- Web-based Workflow Management - Create and manage LangFlow workflows through a web interface

- Snapshot Operations - Save and load workflow snapshots

- Prompt Management - Manage and version control your AI prompts

- Real-time Execution - Execute workflows in real-time with live results

### API Endpoints

The application provides various endpoints for:

- Workflow execution and management
- Snapshot creation and restoration
- Prompt template management
- System monitoring
