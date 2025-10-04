import subprocess

def run_command(cmd: str):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        success = result.returncode == 0
        output = result.stdout if success else result.stderr
        return success, output
    except Exception as e:
        return False, str(e)
