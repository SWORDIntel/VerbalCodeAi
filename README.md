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

## Getting Started

### Prerequisites

* Python 3.11.6 (tested and recommended version)
* [OpenVINO™ Toolkit](https://docs.openvino.ai/latest/openvino_docs_install_guides_installing_openvino.html) **(for accelerated inference)**
* [Ollama](https://ollama.com/download) (for local model execution)

> **Note:** The application has been specifically tested with Python 3.11.6 on Windows and Linux. While it may work with other versions, for the best experience, we recommend using the tested version.

### Installation

#### Windows

1. Clone the repository:

   ```bash
   git clone https://github.com/vibheksoni/VerbalCodeAi.git
   cd VerbalCodeAi
   ```

2. Run the setup script (includes OpenVINO installation):

   ```bash
   setup_windows.bat
   ```

#### Linux/macOS

1. Clone the repository:

   ```bash
   git clone https://github.com/vibheksoni/VerbalCodeAi.git
   cd VerbalCodeAi
   ```

2. Make the setup script executable and run it (installs OpenVINO):

   ```bash
   chmod +x setup_linux.sh
   ./setup_linux.sh
   ```

### Manual Installation

If you prefer to set up manually:

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   * Windows: `venv\Scripts\activate`
   * Linux/macOS: `source venv/bin/activate`

3. Install dependencies (including OpenVINO Python packages):

   ```bash
   pip install -r requirements.txt
   pip install openvino openvino-dev[onnx]
   ```

4. Create a `.env` file with your configuration (see `.env.example` for reference)

## Usage

### Starting the Application

After installation, activate your virtual environment and run:

```bash
python app.py
```

*(... rest of Usage remains unchanged ...)*

## Configuration

### Supported LLM & Inference Providers

* **Ollama**: Local models (default)
* **OpenVINO**: Hardware-accelerated inference on Intel® CPUs, GPUs, VPUs
* **Google AI**: Cloud-based models (requires API key)
* **OpenAI**: OpenAI models for both chat and embeddings (requires API key)
* **Anthropic**: Claude models for chat (requires API key)
* **Groq**: High-performance LLMs with low latency (requires API key)
* **OpenRouter**: Various cloud models (requires API key)

#### Configuring OpenVINO

To enable OpenVINO for inference, add the following to your `.env`:

```dotenv
# Inference Accelerator
INFERENCE_PROVIDER=openvino

# Optional: specify device (CPU | GPU | VPU)
OPENVINO_DEVICE=CPU
```

### Performance Settings

* **LOW**: Minimal resource usage, suitable for low-end systems
* **MEDIUM**: Balanced resource usage, suitable for most systems
* **MAX**: Maximum resource usage, suitable for high-end systems
* **OPENVINO**: Select this mode to leverage OpenVINO optimizations (e.g., FP16, INT8 quantization)

*(... rest unchanged ...)*

## Acknowledgements

* [OpenVINO Toolkit](https://docs.openvino.ai/) for providing optimized inference engines
* [Ollama](https://ollama.com/)
* [Tree-sitter](https://tree-sitter.github.io/tree-sitter/)
* All the open-source libraries that make this project possible

---

Made with ❤️ by <a href="https://github.com/vibheksoni">Vibhek Soni</a>
