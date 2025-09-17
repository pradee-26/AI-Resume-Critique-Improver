import subprocess

def ollama_run(prompt: str) -> str:
    try:
        proc = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            timeout=120
        )
        return proc.stdout.strip()
    except Exception as e:
        return f"Exception: {str(e)}"
