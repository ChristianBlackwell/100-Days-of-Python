## 📦 How to Create a Virtual Environment (venv) per Project on macOS

Assuming you're already inside your project folder, for example:
cd projects/day18

### ✅ 1. Create the virtual environment

Use Python 3’s built-in venv module:
python3 -m venv venv
This creates a folder named venv/ inside your project directory.

### ✅ 2. Activate the venv

On macOS:
source venv/bin/activate

Your terminal prompt should change and show something like:
(venv) user@MacBook-Pro …

Now any Python or pip commands run inside this isolated environment.

### ✅ 3. Install packages (if needed)

Example:
pip install matplotlib

### ✅ 4. Deactivate when done

To leave the environment:
deactivate
