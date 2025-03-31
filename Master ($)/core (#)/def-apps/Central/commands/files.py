from colorama import init, Fore
import os
import subprocess
init()

def handle_open(file_path: str, app: str):
  try:
    if not os.path.isabs(file_path):
      raise ValueError("Use absolute routes! e.g: 'C:/folder/file.txt' or '/home/user/file.txt'")
    
    if not os.path.exists(file_path):
      raise FileNotFoundError(f"The file '{file_path}' does not exist")
        
    if os.name == 'nt':  # Windows
      subprocess.run(f'"{app}" "{file_path}"', shell=True)
    else:  # Linux/macOS
      subprocess.run([app, file_path])
        
    print(Fore.GREEN + f"[v] Opened: '{file_path}' with {app}" + Fore.RESET)
    
  except Exception as e:
    print(Fore.RED + f"Error: {e}" + Fore.RESET)

def handle_exe(program: str):
    try:
        subprocess.Popen(program, shell=True)
        print(Fore.GREEN + f"Executing'{program}'..." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Fore.RESET)
