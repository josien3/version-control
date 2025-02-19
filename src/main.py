from datetime import datetime

# Get current date and time
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write to docs/version.md (not the docs/ folder!)
with open("docs/version.md", "w") as file:
    file.write(f"Last updated: {now}\n")

print("version.md updated successfully.")




