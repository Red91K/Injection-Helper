import json
import subprocess
import platform

try:
   with open("config.json","r") as f:
      SETTINGS = json.load(f)
except FileNotFoundError:
   print("CONFIG FILE NOT FOUND!")

def interactive_mode():
   while True:
      user_input = input("Enter a command to inject. Enter nothing to exit:\n")
      if user_input == "":
         break
      else:
         out_str = SETTINGS["Injection-Template-String"].replace(SETTINGS["String-To-Replace"],user_input)
         print(out_str)
         if SETTINGS["Paste-To-Clipboard"]:
            if platform.system() == "Darwin":  # MacOS
               subprocess.run("pbcopy", universal_newlines=True, input=out_str)
            elif platform.system() == "Linux":
               subprocess.run("xclip -selection clipboard", universal_newlines=True, input=out_str, shell=True)
            elif platform.system() == "Windows":
               subprocess.run("clip", universal_newlines=True, input=out_str, shell=True)
            print("OUTPUT COPIED TO CLIPBOARD!\n")

def modify_string_template():
   print(f"Your current template string is '{SETTINGS["Injection-Template-String"]}'")
   print(f"Injection-Helper will replace the string {SETTINGS["String-To-Replace"]} with a specific command.")
   
   new_template = input("Enter a new string template:\n")
   SETTINGS["Injection-Template-String"] = new_template
   
   with open("config.json","w") as f:
      json.dump(SETTINGS,f,indent=3)

def help():
   print("\n")
   print("Injection-Helper 2024")
   print("This is a tool to make crafting command injection payloads easier.")
   print("Injection-Helper allows you to configure a template string for your command injection attack once, then generate command-injection strings for custom payloads with ease")
   print("""
How to Use:
-----------
Run the tool and select an option from the menu:
1. For Interactive Mode, select option 1. You will enter the payload you want to execute, and the program will wrap it inside the command injection attack string.
2. To modify the template string, select option 2. You will be asked to enter a new template string.""")   

   print("\n\n")

if __name__ == "__main__":
   options = {
      "1": interactive_mode,
      "2": modify_string_template,
      "3": help
   }
   print("Choose an option:")
   while True:
      for key, value in options.items():
         print(f"[{key}]: {value.__name__}")
   
      user_input = input("Enter an option #: ")
      if user_input in options:
         options[user_input]()
         
   