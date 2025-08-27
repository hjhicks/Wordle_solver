import subprocess
import sys
import os

def run_wordle_solver(known, has, allowed):
    cmd = [sys.executable, os.path.join(os.path.dirname(__file__), '..', 'wordle.py')]
    input_str = f"{known}\n{has}\n{allowed}\n"
    try:
        result = subprocess.run(
            cmd,
            input=input_str.encode(),
            capture_output=True,
            check=True
        )
        return result.stdout.decode(errors='replace')
    except Exception as e:
        return f"Error running solver: {e}"
