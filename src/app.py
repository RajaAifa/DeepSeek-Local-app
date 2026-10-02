import gradio as gr
from utils.model_handler import generate_code
import os

# Custom CSS with Tailwind
CSS = """
@import url('https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css');

.gradio-container {
    @apply bg-gradient-to-br from-gray-900 to-blue-900 min-h-screen;
}

.dark .input-text textarea {
    @apply bg-gray-800 text-white border-gray-700 !important;
}

.code-output pre {
    @apply bg-gray-800 p-4 rounded-lg text-green-400 overflow-x-auto;
}
"""

with gr.Blocks(title="DeepSeek Local Coder", css=CSS) as app:
    
    with gr.Row(equal_height=True, variant="panel"):
        gr.Markdown("""<h1 style="text-align: center; color: white; font-size: 1.875rem;">🚀 DeepSeek Code Generator</h1>""")
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("""<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
            <rect width="200" height="200" rx="30" fill="#1a1a2e"/>
            <path d="M100 50 L150 100 L100 150 L50 100 Z" fill="none" stroke="#00dcff" stroke-width="8"/>
            <circle cx="100" cy="100" r="20" fill="#00dcff" opacity="0.8"/>
            <text x="100" y="180" font-family="Arial" font-size="20" fill="white" text-anchor="middle">DeepSeek</text>
            </svg>""")
            gr.Markdown("### ⚙️ Settings")
            language = gr.Dropdown(
                choices=["Python", "JavaScript", "Go", "Rust", "Java"],
                value="Python",
                label="Language",
                elem_classes="bg-gray-800 text-white"
            )
            temperature = gr.Slider(0, 1, value=0.3, label="Creativity Level")
            
        with gr.Column(scale=3):
            prompt = gr.Textbox(
                label="Describe your code needs",
                placeholder="Ex: 'A Python function to calculate prime numbers'",
                lines=3,
                elem_classes="input-text"
            )
            output = gr.Code(
                label="Generated Code",
                language=language.value.lower(),
                elem_classes="code-output"
            )
    
    with gr.Row():
        submit_btn = gr.Button(
            "Generate Code →",
            variant="primary",
            elem_classes="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-full"
        )
        clear_btn = gr.Button("Clear", elem_classes="bg-gray-600 hover:bg-gray-700")

    submit_btn.click(
        fn=generate_code,
        inputs=[prompt, language, temperature],
        outputs=output
    )
    
    clear_btn.click(lambda: [None, None, 0.3], outputs=[prompt, output, temperature])

if __name__ == "__main__":
    app.launch(server_name="127.0.0.1", server_port=7860, share=True)

