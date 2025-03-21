from datetime import datetime
import os

# Get current date and time
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Get the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
# Navigate from src folder to docs folder (with 's')
version_file_path = os.path.join(script_dir, "..", "docs", "version.md")

# Write to the file using the absolute path
with open(version_file_path, "w") as file:
    file.write(f"Last updated: {now}\n")

print(f"version.md updated successfully at {version_file_path}")


