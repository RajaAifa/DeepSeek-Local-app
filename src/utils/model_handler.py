import ollama
import dotenv
import os



def generate_code(prompt: str, language: str, temperature: float):
    system_prompt = f"""You are an expert developer in the {language} language. Follow these rules:
    1. Generate clean, production-ready code
    2. Include comments for complex sections
    3. Use modern language features
    4. Add type hints where applicable
    5. All text that's not a code should be made as a comment
    6. Give me the code without introduction or conclusion"""
    dotenv.load_dotenv()
    response = ollama.generate(
        model=os.getenv('DEFAULT_MODEL'),
        system=system_prompt,
        prompt=prompt,
        options={
            'temperature': temperature,
            'num_predict': 512,
            'top_k': 50,
            'stop': ['</end>']
        }
    )
    return response['response']