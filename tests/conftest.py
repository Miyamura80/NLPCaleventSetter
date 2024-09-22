import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Add the src and deps directories to the Python path
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
deps_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "deps"))
sys.path.insert(0, src_path)
sys.path.insert(0, deps_path)

# Print the Python path for debugging
print("Python path:", sys.path)

# Print the contents of the deps directory
print("Contents of deps directory:")
for root, dirs, files in os.walk(deps_path):
    level = root.replace(deps_path, '').count(os.sep)
    indent = ' ' * 4 * (level)
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 4 * (level + 1)
    for f in files:
        print(f"{subindent}{f}")
