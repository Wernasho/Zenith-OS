import random
import os
import subprocess
from commands.files import handle_open, handle_exe
from commands.help import cmds_help, cmds_howto, how_to
from utils.paths import conv
from utils.easter_eggs import facts, others, others_2 
from colorama import init, Fore, Back, Style

init()
print(Fore.GREEN + """
/==============================/
|                              |
| TomatOS v0.1                 |
| TomatOS served fresh!        |
|                              |
/==============================/""" + Style.RESET_ALL)

while True:
  current_path = "" or "$>#"
  cmd = input(Fore.GREEN + f"TomatOS>User {current_path}: " + Style.RESET_ALL).lower()
  cmds = ["conv", "wconv", "lconv", "iConv", "facts", "make", "open", "conv_m", "mconv",
   "del", "chdir", "howto", "simcrash"]
  fact_to_show = random.choice(facts)
  messages = {5: "That does not count as a Tomato... Nor as a valid input...", 4: "These tomatOS are for the spaghetti tomato sauce only!"}

  if cmd == "conv":
    targ_imp = input("Enter OS to translate (windows, Linux, Mac OS)").lower().strip()
    path_input = input("Enter Path to transalte:").lower()
    conv(path_input, targ_imp) 
  elif cmd == "facts":
    print(Fore.CYAN + Back.WHITE + fact_to_show + Style.RESET_ALL)
  elif cmd == others[3]:
    print(Fore.MAGENTA + others_2[2] + Fore.RESET)
  elif cmd == others[1] or cmd == others[2]:
    print(Fore.MAGENTA + others_2[1] + Fore.RESET)
  elif cmd == others[0]:
    print(Fore.MAGENTA + others_2[0] + Fore.RESET)
  elif cmd == others[3]:
    print(Fore.MAGENTA + others_2[2] + Fore.RESET)
  elif cmd == others[4]:
    print(Fore.MAGENTA + others_2[3] + Fore.RESET)
  elif cmd == "exit":
    print("Byeeeeeeeeee!")
    break 
  elif cmd == "simcrash": #100 líneas... ¡TomatOS ya tiene el tamaño de un tomate cherry!
    print("""
  x_x
  Your TomatOS got rotten!
    Your PC has ran into a problem, we're trying to fix it :3.""")
  elif cmd == "gh":
    print(f"""comands: 
    {cmds}""")
  elif cmd.startswith("help"):
    try:
      command = cmd.split(" ")[1]
      print(cmds_help.get(command, "Comnand not found."))
    except IndexError:
      print("Use: help <command>. Available coommands:", list(cmds_help.keys()))
  elif cmd.startswith("open"):
    try:
      parts = cmd[len("open"):].strip().split("**", 1)
      if len(parts) != 2:
        raise ValueError("Formato incorrecto")
      file_part = parts[0].strip()
      if not file_part.startswith("*"):
        raise ValueError("Falta '*' antes del archivo")
      file_path = file_part[1:].strip() 
      app = parts[1].strip()
      handle_open(file_path, app)
    except Exception as e:
      print(Fore.RED + f"Error: {e}. Formato correcto: open *archivo **app" + Fore.RESET)
  elif cmd.startswith("exe"):
    program = cmd.split(" ", 1)[1]
    handle_exe(program)