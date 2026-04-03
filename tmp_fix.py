import os
import glob
import re

titles_dir = r"e:\Notes\reviews\Movie-Reviews\titles"
files = glob.glob(os.path.join(titles_dir, "*.md"))

status_regex = re.compile(r"\|\s*Status\s*\|.*", re.DOTALL)

for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    lines = content.split('\n')
    new_lines = []
    skip = False
    
    # We want to just find the line starting with "| Status" and replace everything until the next line starting with "| Watch" or similar.
    # Actually, simpler:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    new_content = re.sub(r"\|\s*Status\s*\|.*?\|\s*Watch Start Date\s*\|", 
                         "| Status             | Watched                     |\n| Watch Start Date   |", 
                         content, flags=re.DOTALL)
    
    # Note: If status is Watching, we don't want to replace with Watched.
    # Luckily, "Dasim" is the only one watching.
    if os.path.basename(f) == "dasim.md":
        new_content = re.sub(r"\|\s*Status\s*\|.*?\|\s*Watch Start Date\s*\|", 
                         "| Status             | Watching                    |\n| Watch Start Date   |", 
                         content, flags=re.DOTALL)
                         
    if content != new_content:
        with open(f, "w", encoding="utf-8") as file:
            file.write(new_content)
        print(f"Fixed {os.path.basename(f)}")

