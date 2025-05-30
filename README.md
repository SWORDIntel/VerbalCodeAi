# VerbalCodeAI 🤖

[![GitHub stars](https://img.shields.io/github/stars/vibheksoni/VerbalCodeAi?style=social)](https://github.com/vibheksoni/VerbalCodeAi/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/vibheksoni/VerbalCodeAi?style=social)](https://github.com/vibheksoni/VerbalCodeAi/network/members)
[![GitHub issues](https://img.shields.io/github/issues/vibheksoni/VerbalCodeAi)](https://github.com/vibheksoni/VerbalCodeAi/issues)
[![GitHub license](https://img.shields.io/github/license/vibheksoni/VerbalCodeAi)](https://github.com/vibheksoni/VerbalCodeAi/blob/master/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.11.6-blue)](https://www.python.org/downloads/release/python-3116/)
[![OpenVINO Support](https://img.shields.io/badge/Inference-OpenVINO-orange)](https://docs.openvino.ai/)
[![Website](https://img.shields.io/badge/website-verbalcode.xyz-brightgreen)](https://verbalcode.xyz) <a href="https://discord.gg/KpjSDEwWCF" target="_blank"> <img src="https://img.shields.io/static/v1?label=Discord&message=Join%20Us&color=7289DA&logo=discord&logoColor=white&style=for-the-badge" alt="Join our Discord"/> </a>

Join our Discord server to hang out, ask questions, or offer help! We're currently looking for assistance in setting up the server, so if you're experienced with Discord setup, your help would be greatly appreciated! Click [here](https://discord.gg/KpjSDEwWCF) to join.

Ever felt lost in a complex codebase? Wish you had a smart assistant to help you navigate and understand code right in your terminal? VerbalCodeAI is here to help! This powerful AI-powered tool acts as your personal code companion, leveraging advanced embedding techniques, Large Language Model (LLM) integration, **and OpenVINO accelerated inference**. It offers intelligent code analysis, helps you search and understand your project, and provides assistance directly within your command-line interface, making your development workflow smoother and more efficient.

```yaml
.       .      .          .    .--.        .           .
 \     /       |          |   :            |          / \     o
  \   /.-. .--.|.-.  .-.  |   |    .-.  .-.| .-.     /___\    .
   \ /(.-' |   |   )(   ) |   :   (   )(   |(.-'    /     \   |
    '  `--''   '`-'  `-'`-`-   `--'`-'  `-'`-`--'  '       `-' `-'
                       [AI Assistant for Code]
```

<div align="center">
  <img src="Showcase/VerbalCodeShowcase.gif" alt="VerbalCodeAI Showcase" style="max-width: 800px; max-height: 400px; width: 100%; height: auto;"/>
</div>

<details>
<summary><strong>Table of Contents</strong></summary>

* [VerbalCodeAI 🤖](#verbalcodeai-)

  * [Getting Started](#getting-started)

    * [Prerequisites](#prerequisites)
    * [Installation](#installation)

      * [Windows](#windows)
      * [Linux/macOS](#linuxmacos)
    * [Manual Installation](#manual-installation)
  * [Usage](#usage)

    * [Starting the Application](#starting-the-application)
    * [Indexing a Project](#indexing-a-project)
    * [Main Menu Options](#main-menu-options)
    * [Agent Mode Tools](#agent-mode-tools)
    * [HTTP API Server](#http-api-server)
    * [MCP Integration](#mcp-integration)
  * [Configuration](#configuration)

    * [Supported LLM & Inference Providers](#supported-llm--inference-providers)
    * [Performance Settings](#performance-settings)
    * [UI Settings](#ui-settings)
  * [Video Showcase](#video-showcase)
  * [Image Showcase](#image-showcase)
  * [Project Structure](#project-structure)
  * [Contributing](#contributing)
  * [License](#license)
  * [Links](#links)
  * [Acknowledgements](#acknowledgements)

</details>

---

## Getting Started

### Prerequisites

* **Python 3.11.6** (tested and recommended)
* **OpenVINO™ Toolkit** – for accelerated inference:
  [https://docs.openvino.ai/latest/openvino\_docs\_install\_guides\_installing\_openvino.html](https://docs.openvino.ai/latest/openvino_docs_install_guides_installing_openvino.html)
* **Ollama** – for local LLM execution:
  [https://ollama.com/download](https://ollama.com/download)

> **Note:** Tested on Windows and Linux (Debian/RHEL). Other platforms may work but aren’t officially supported.

### Installation

#### Windows

1. Clone the repo:

   ```bash
   git clone https://github.com/vibheksoni/VerbalCodeAi.git
   cd VerbalCodeAi
   ```
2. Run the installer (includes OpenVINO pip packages):

   ```bash
   setup_windows.bat
   ```

#### Linux/macOS

1. Clone the repo:

   ```bash
   git clone https://github.com/vibheksoni/VerbalCodeAi.git
   cd VerbalCodeAi
   ```
2. Make and run the installer (also installs OpenVINO):

   ```bash
   chmod +x setup_linux.sh
   ./setup_linux.sh
   ```

### Manual Installation

If you prefer manual steps:

1. Create a venv:

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```
2. Install dependencies + OpenVINO:

   ```bash
   pip install -r requirements.txt
   pip install openvino openvino-dev[onnx]
   ```
3. Copy `.env.example` → `.env` and set your keys/providers.

---

## Usage

### Starting the App

```bash
python app.py
```

You’ll land in the TUI main menu:

* **Chat with AI** – Ask questions about your code
* **Agent Mode** – Tool-driven exploration
* **Reindex Project** – Refresh embeddings
* **Project Info** – Overview & stats
* **Settings** – Swap LLMs / inference backends
* **Exit** – Quit

### Indexing a Project

Select a directory; VerbalCodeAI builds embeddings & metadata for fast semantic search.

### Agent Mode Tools

* **Search**: `embed_search`, `semantic_search`, `grep`, `regex_search`
* **File Ops**: `read_file`, `file_stats`, `directory_tree`, `describe_file`
* **Code Analysis**: `find_functions`, `find_classes`, `cross_reference`, `explain_code`
* **VCS**: `git_history`, `diff_search`, `blame_search`
* **System**: `run_command`, `read_terminal`, `kill_terminal`
* **Memory**: `add_memory`, `get_memories`
* **Web**: `google_search`, `ddg_search`, `fetch_webpage`

> **Tip:** Agent Mode uses fewer API calls vs Chat Mode—ideal for cloud quotas.

### HTTP API Server

Start programmatically:

```bash
python app.py --serve 8000
```

Endpoints:

* `GET  /api/health`
* `POST /api/initialize`
* `POST /api/ask`
* `POST /api/index/start`
* `GET  /api/index/status`

> Use `HTTP_ALLOW_ALL_ORIGins=TRUE` in `.env` to expose beyond localhost.

### MCP Integration

Leverage the Model Context Protocol:

1. Ensure HTTP server is running on port 8000.
2. Run the MCP wrapper:

   ```bash
   python mcp_server.py
   ```
3. Configure your assistant (Claude Desktop, Cursor, etc.) to point at `http://localhost:8000`.

---

## Configuration

### Supported LLM & Inference Providers

* **Ollama** – Local LLM
* **OpenVINO** – Intel-accelerated inference (CPU/GPU/VPU)
* **Google AI** – Cloud LLMs (API key)
* **OpenAI** – GPT-series (API key)
* **Anthropic** – Claude models (chat)
* **Groq** – Ultra-low latency LLMs
* **OpenRouter** – Multi-provider gateway

#### Enabling OpenVINO

In your `.env`:

```dotenv
# Use OpenVINO for inference
INFERENCE_PROVIDER=openvino

# Device options: CPU | GPU | VPU
OPENVINO_DEVICE=CPU
```
