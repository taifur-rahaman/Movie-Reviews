import os
import glob
import re
import json

titles_dir = r"e:\Notes\reviews\Movie-Reviews\titles"
files = glob.glob(os.path.join(titles_dir, "*.md"))

status_regex = re.compile(r"\|\s*Status\s*\|\s*(.*?)\s*\|")
runtime_regex = re.compile(r"\|\s*Runtime\s*\|\s*(\d+)h\s*(\d+)m")
genre_regex = re.compile(r"\|\s*Genre\s*\|\s*(.*?)\s*\|")

total_minutes = 0
watched_files = []
watching_files = []
weird_files = []

for f in files:
    filename = os.path.basename(f)
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
        
        status_match = status_regex.search(content)
        status = status_match.group(1).strip() if status_match else "MISSING"
        
        runtime = 0
        runtime_match = runtime_regex.search(content)
        if runtime_match:
            runtime = int(runtime_match.group(1)) * 60 + int(runtime_match.group(2))
            total_minutes += runtime
        
        if status.startswith("Watched") or status == "Completed":
            watched_files.append((filename, runtime))
        elif status == "Watching":
            watching_files.append((filename, runtime))
            
        if status not in ["Watched", "Watching"]:
            weird_files.append((filename, status))

result = {
    "total_files": len(files),
    "watched_count": len(watched_files),
    "watching_count": len(watching_files),
    "weird_files": weird_files,
    "total_runtime_minutes": total_minutes
}
print(json.dumps(result, indent=2))
