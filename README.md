# 🤖 DeepSeek Local AI Code Generator

A **local and privacy-friendly AI code generation application** powered by **DeepSeek Coder V2**, **Ollama**, and **Gradio**.

This application allows users to describe what they want in natural language and automatically generate code in different programming languages — **without relying on cloud APIs or sending prompts to external AI services**.

---

## ✨ Overview

**DeepSeek Local AI Code Generator** is an AI-powered coding assistant designed to run locally on your computer.

Instead of using online AI APIs, the application uses **DeepSeek Coder V2** through **Ollama** to generate code locally.

Simply enter a request such as:

> Create a Python function that checks whether a number is prime.

The application generates the corresponding code directly on your computer.

---

## 🔐 Privacy First

All AI inference is performed locally through Ollama.

- ✅ No API key required
- ✅ No cloud AI service required
- ✅ No prompts sent to external AI APIs
- ✅ Your code remains on your computer
- ✅ Can work offline after the initial installation and model download

---

## 🚀 Features

- 🤖 **AI Code Generation** — Generate source code from natural-language descriptions.
- 🧠 **DeepSeek Coder V2** — Uses a coding-focused AI model for code generation.
- 💻 **Multiple Programming Languages** — Python, JavaScript, Java, Go, Rust.
- 🎛️ **Adjustable Creativity** — Control the model's creativity/temperature level.
- 🔒 **Local & Private** — AI inference is performed locally through Ollama.
- 🌐 **Interactive Web Interface** — Built with Gradio.
- 🎨 **Modern Dark Interface** — Custom styling for a clean and modern user experience.
- 📝 **Syntax Highlighting** — Generated code is displayed in a readable code block.
- ⚡ **No External API Keys** — No OpenAI, Gemini, or other cloud AI credentials are required.

---

## 🏗️ Architecture

```text
                 ┌─────────────────────┐
                 │        User         │
                 │                     │
                 │ Natural Language    │
                 │ Coding Prompt       │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │       Gradio        │
                 │   Web Interface     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Prompt Handler    │
                 │                     │
                 │ Language + Prompt   │
                 │ + Creativity Level  │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │       Ollama        │
                 │   Local AI Runtime  │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ DeepSeek Coder V2   │
                 │    Local Model      │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Generated Code    │
                 │                     │
                 │ Python / JS / Go    │
                 │ Rust / Java         │
                 └─────────────────────┘
```

---

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| 🐍 Python | Application development |
| 🎨 Gradio | Interactive web interface |
| 🧠 DeepSeek Coder V2 | Local AI code generation |
| 🦙 Ollama | Local AI model execution |
| 🎨 CSS | User interface customization |
| ⚙️ python-dotenv | Environment configuration |

---

## 📋 Prerequisites

Before running the project, make sure you have:

- Python 3.9 or newer
- Ollama installed
- DeepSeek Coder V2 installed through Ollama
- Git installed

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/deepseek-local-app-main.git
cd deepseek-local-app-main
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🦙 Ollama Setup

Install Ollama and make sure it is running on your computer.

Then download the DeepSeek Coder V2 model:

```bash
ollama pull deepseek-coder-v2
```

Verify that the model is installed:

```bash
ollama list
```

You can also start the Ollama server manually:

```bash
ollama serve
```

---

## ⚙️ Environment Configuration

Create a `.env` file in the root directory:

```env
OLLAMA_HOST=http://localhost:11434
DEFAULT_MODEL=deepseek-coder-v2
```

### Environment Variables

| Variable | Description | Default |
|---|---|---|
| `OLLAMA_HOST` | Address of the local Ollama server | `http://localhost:11434` |
| `DEFAULT_MODEL` | Default AI model | `deepseek-coder-v2` |

---

## ▶️ Running the Application

Navigate to the `src` directory:

```bash
cd src
```

Start the application:

```bash
python app.py
```

Once the application starts, open your browser and visit:

```text
http://127.0.0.1:7860
```

---

## 💡 How to Use

### Step 1 — Select a Programming Language

Choose the programming language you want to generate code for:

- Python
- JavaScript
- Java
- Go
- Rust

### Step 2 — Choose the Creativity Level

Adjust the creativity (temperature) level depending on how deterministic or creative you want the generated response to be.

### Step 3 — Enter Your Prompt

Describe what you want the AI to create. Example:

> Create a Python function that checks whether a number is prime.

### Step 4 — Generate the Code

Click the **Generate Code** button.

The request is sent to your local Ollama server, where DeepSeek Coder V2 generates the requested code.

---

## 🧪 Example Prompts

**🐍 Python**

> Create a Python function that checks whether a number is prime.

**🌐 JavaScript**

> Create a JavaScript function that validates an email address.

**☕ Java**

> Create a Java class representing a bank account with deposit and withdrawal methods.

**🦀 Rust**

> Create a Rust program that reads a file and counts the number of lines.

**🔵 Go**

> Create a Go REST API endpoint that returns a JSON response.

---

## 📁 Project Structure

```text
deepseek-local-app-main/
│
├── src/
│   ├── app.py
│   ├── styles.css
│   │
│   ├── static/
│   │   └── images/
│   │       └── logo.png
│   │
│   └── utils/
│       ├── model_handler.py
│       └── prompts.py
│
├── tests/
│   └── test_app.py
│
├── requirements.txt
├── .env
└── README.md
```

---

## 🔄 Application Workflow

```text
User enters coding request
          │
          ▼
Select programming language
          │
          ▼
Select creativity level
          │
          ▼
Prompt is processed
          │
          ▼
Ollama receives the request
          │
          ▼
DeepSeek Coder V2 generates code
          │
          ▼
Generated code is returned
          │
          ▼
Code displayed in Gradio
```

---

## 🔒 Privacy & Security

The project is designed around local AI processing. Unlike cloud-based coding assistants, it does not require an external AI API.

### Local Processing

```text
Your Computer
     │
     ├── Gradio
     │
     ├── Python Application
     │
     ├── Ollama
     │
     └── DeepSeek Coder V2
```

Your prompts and generated code are processed through the local Ollama server.

### Benefits

- 🔐 Local AI inference
- 🚫 No external AI API required
- 🔑 No API keys required
- 📴 Can operate offline after setup
- 💻 Greater control over your AI environment

> **Note:** Internet access may still be required initially to download Ollama, Python dependencies, and the DeepSeek Coder V2 model.

---

## 🧪 Testing

Tests are located in the `tests` directory.

```bash
python -m pytest
```

If pytest is not installed:

```bash
pip install pytest
```

---

## 🖥️ User Interface

The application provides a simple interface where users can:

- Select the programming language
- Choose the creativity level
- Enter a natural-language coding request
- Generate code
- View the generated code directly in the browser
- Clear the current input and output

---

## 🌟 Why This Project?

Many AI coding assistants rely on cloud services and external APIs. This project provides an alternative by running the AI model locally.

**Cloud-Based AI**

```text
User → Internet → Cloud AI API → Generated Code
```

**DeepSeek Local AI**

```text
User → Local Application → Ollama → DeepSeek Coder V2 → Generated Code
```

This approach gives users greater control over their coding prompts and generated content.

---

## 🚧 Future Improvements

- 💬 Conversation history
- 📂 Code file export
- 📋 Copy-to-clipboard functionality
- 🧪 Automatic code testing
- 🐛 AI-assisted debugging
- 🔍 Code explanation
- 🔄 Code refactoring
- 📊 Model performance comparison
- 🧠 Support for additional local AI models
- 🌐 Multi-language interface
- 📁 Upload and analyze existing source-code files

---

## 🛠️ Troubleshooting

### Ollama is not responding

Make sure Ollama is running:

```bash
ollama serve
```

Then verify the installed models:

```bash
ollama list
```

### DeepSeek Coder V2 is not installed

```bash
ollama pull deepseek-coder-v2
```

### Python dependencies are missing

```bash
pip install -r requirements.txt
```

### Port 7860 is already in use

Stop the application currently using the port, or configure Gradio to use another available port.

---

## 📜 License

This project is intended for educational and research purposes.

If you distribute or modify the project, make sure to comply with the licenses of the libraries, frameworks, models, and other third-party components used by the application.

---

## 👨‍💻 Author

**Raja Aifa**

🎓 Master's Degree in Web Service and Multimedia

💻 AI & Web Development Enthusiast

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 🚀 Project Summary

DeepSeek Local AI Code Generator combines:

- 🧠 DeepSeek Coder V2
- 🦙 Ollama
- 🎨 Gradio
- 🐍 Python

to provide a local AI-powered code generation experience without requiring cloud AI APIs.

> 💡 Describe your idea → Choose a programming language → Generate code locally. 🚀
