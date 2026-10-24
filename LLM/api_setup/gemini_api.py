from dotenv import load_dotenv
from google import genai

# Load variables from the .env file
load_dotenv() 

# The client automatically finds GEMINI_API_KEY in the environment
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash", 
    contents="how to use virtual environment in python, to use in windows just give 3 simple commands that to i run " \
    "in a wsl Ub 22.04 terminal to create a virtual environment and activate it, and then install the required packages in it. " \
)

print("Response:", response.text)

# ***o/p*** 
# Response: Here are the 3 commands to run in your Ubuntu 22.04 terminal:

# 1. **Create the environment:**
#    ```bash
#    python3 -m venv myenv
#    ```

# 2. **Activate it:**
#    ```bash
#    source myenv/bin/activate
#    ```

# 3. **Install your packages:**
#    ```bash
#    pip install <package_name>
#    ```
#    *(Replace `<package_name>` with your library, e.g., `requests`, `numpy`, or `-r requirements.txt`)*

# ---
# *(Note: If step 1 gives an error, run `sudo apt update && sudo apt install python3-venv -y` once to enable venv support on Ubuntu).*