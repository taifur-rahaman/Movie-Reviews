import os
import glob
import re

titles_dir = r"e:\Notes\reviews\Movie-Reviews\titles"
files = glob.glob(os.path.join(titles_dir, "*.md"))

status_regex = re.compile(r"\|\s*Status\s*\|\s*(.*)\s*\|")

genres_regex = re.compile(r"\|\s*Genre\s*\|\s*(.*)\s*\|")
rating_regex = re.compile(r"\|\s*Rating\s*\|\s*(.*)\s*\|")

for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
        status_match = status_regex.search(content)
        status = status_match.group(1).strip() if status_match else "MISSING"
        if status not in ["Watched", "Watching"]:
            print(f"File {os.path.basename(f)} has weird status: '{status}'")
