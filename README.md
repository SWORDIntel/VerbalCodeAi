Skip to content
Navigation Menu
SWORDIntel
VerbalCodeAi

Type / to search
Code
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
VerbalCodeAi
/
README.md
in
master

Edit

Preview
Indent mode

Spaces
Indent size

2
Line wrap mode

Soft wrap
Editing README.md file contents
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
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

Use Control + Shift + m to toggle the tab key moving focus. Alternatively, use esc then tab to move to the next interactive element on the page.
Aucun fichier choisi
Attach files by dragging & dropping, selecting or pasting them.
Editing VerbalCodeAi/README.md at master · SWORDIntel/VerbalCodeAi
