def conv(path: str, target: str):
  parts = path.split(">")
  if target == "windows":
    core = parts[1] = "Users\\(username)"
    if parts[0] == "$":
      drive = "C:"
    elif parts[0] == "0":
      dirve = "D:"
    elif parts[0] == "1":
      drive = "E:"
    elif parts[0] == "2":
      drive: "F:"
    else:
      drive = "(IDK, why do you have so many drives dude?):"
    print(f"{drive}\\{'\\'.join(parts[1:])}")
  elif target == "linux":
    print(f"/{'/'.join(parts).replace("$", "root").replace("#", "core")}")
  elif target == "macos":
    print(f"")
  else:
    print("That doesn't count as a tomato... Nor does it count as a valid input... Select a supported OS: \nWindows\nLinux\nMac OS")
