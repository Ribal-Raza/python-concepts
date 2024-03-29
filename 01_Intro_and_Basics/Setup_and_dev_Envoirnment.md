## Python Setup and First Program
**Table of Contents**  
* [1. Requirements to run a Python program](#1-requirements-to-run-a-python-program) 
* [2. Installing Python and setting up VS Code](#2-installing-python-and-setting-up-vs-code) 
	* [Windows](#windows)
	* [macOS](#macos) 
	* [Linux](#linux)
* [3. Creating your first  Python program](#3-creating-your-first-python-program) 
* [4. Useful VS Code extensions for Python](#4-useful-vs-code-extensions-for-python) 
	* [Some tips](#remember)
* [REPL](#repl) 
* [Purpose of REPL](#purpose-of-repl) 
* [How to Open Python REPL in VS Code](#how-to-open-python-repl-in-vs-code) 
*  [Doing Calculations in REPL](#doing-calculations-in-repl) 
*  [Additional Tips](#additional-tips) 
*  [Remember](#remember-1)

### **1. Requirements to run a Python program**

  

-  **Python interpreter:** This is the software that reads and executes Python code. You can download it for free from the official Python website ([https://www.python.org/downloads/](https://www.python.org/downloads/)).

-  **Text editor or IDE:** A text editor is a basic tool for writing code, while an Integrated Development Environment (IDE) provides more advanced features like code completion, debugging, and project management. VS Code is a popular and versatile choice for Python development.

  

### **2. Installing Python and setting up VS Code:**

  

**Windows:**

  

1. Download and install the latest Python version from [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/).

2. Install VS Code from [https://code.visualstudio.com/](https://code.visualstudio.com/).

3. Add python installation path to windows envoirnment variables.

4. Open VS Code and install the Python extension from the Extensions marketplace (Ctrl+Shift+X).

5. Select the Python interpreter you installed (Ctrl+Shift+P, then type "Python: Select Interpreter").

  

**macOS:**

  

1. Download and install Python from [https://www.python.org/downloads/macos/](https://www.python.org/downloads/macos/).

2. Install VS Code from [https://code.visualstudio.com/](https://code.visualstudio.com/).

3. Follow the same steps as Windows to install the Python extension and select the interpreter.

  

**Linux:**

  

1. Most Linux distributions come with Python pre-installed. Check using `python --version` in the terminal. If not installed, use your package manager (e.g., `sudo apt install python3` on Ubuntu).

2. Install VS Code following instructions for your distribution.

3. Install the Python extension and select the interpreter as in Windows and macOS.

  

### **3. Creating your first Python program:**

  

1. Open VS Code and create a new file (Ctrl+N).

2. Save the file with a `.py` extension (e.g., `hello.py`).

3. Write your Python code:

  

```python

print("Hello, world!")

```

4. Run the program:

  

-  **VS Code:** Right-click within the editor and select "Run Python File in Terminal".

-  **Terminal:** Navigate to the file's directory and type `python hello.py`(In this, if your are in python-concepts working directory, run `python 01_Intro_and_Basics/1_hello.py` command)

  

### **Useful VS Code extensions for Python:**

  

-  **Pylance:** Provides intelligent code completion, type checking, and linting.

-  **Python Indent:** Automatically formats Python code for proper indentation.

-  **Jupyter:** Enables interactive Python coding and visualization within VS Code.

-  **GitLens:** Integrates Git version control features directly into the editor.

-  **Code Runner:** Allows running Python code snippets directly in the editor.

  

**Remember:**

  

-  **Virtual environments:** Isolate project-specific Python environments to avoid conflicts between different projects and libraries. You can create virtual environments using tools like `venv` or `virtualenv`.

-  **Official documentation:** Refer to the Python documentation ([https://docs.python.org/](https://docs.python.org/)) and VS Code Python extension documentation ([https://code.visualstudio.com/docs/python/python-tutorial](https://code.visualstudio.com/docs/python/python-tutorial)) for more details and latest updates.

  

## **REPL**

  

**REPL** stands for **Read-Eval-Print Loop**. It's an interactive environment where you can type Python code, have it executed immediately, and see the results. It's like having a conversation with Python, where you ask it questions and it responds with answers.

  

**Purpose of REPL:**

  

-  **Experimenting with code:** Try out code snippets, test ideas, and explore Python's features without creating separate files.

-  **Learning Python:** Get immediate feedback on your code, making it an excellent tool for learning and practicing Python.

-  **Debugging:** Inspect variables and step through code line by line to identify errors.

-  **Quick calculations and tasks:** Perform simple calculations or tasks without writing a full-fledged script.

  

### **How to Open Python REPL in VS Code:**

  

1.  **Select Python Interpreter:**

- Press **Ctrl+Shift+P** (Windows/Linux) or **Cmd+Shift+P** (macOS).

- Type **Python: Select Interpreter** and choose the appropriate interpreter.

2.  **Open REPL:**

- There are two main ways to open REPL:

-  **Terminal Panel:**

- Open the **Terminal** panel (**Ctrl+`** or **View > Terminal**).

- Type `python` and press Enter.

- You'll see the `>>>` prompt, indicating you're in the REPL.

-  **Python Interactive Window:**

- Press **Ctrl+Shift+P** (Windows/Linux) or **Cmd+Shift+P** (macOS).

- Type **Python: Start REPL** and select the option.

- This opens a separate interactive window with code completion and other features.

### **Doing Calculations in REPL:**

- Type expressions directly at the prompt and press Enter:

```python

>>> 2 + 2

4

>>> 3 * 5

15

>>> 10 / 2

5.0

```

- Use variables to store values:

```python

>>> x = 10

>>> y = 5

>>> x + y

15

```

  

### **Additional Tips:**

  

- Use the **up** and **down** arrow keys to navigate through your command history.

- Use **Tab** for code completion.

- Use **Ctrl+C** (Windows/Linux) or **Cmd+C** (macOS) to interrupt a running process.

- Use **help(function_name)** or **function_name?** to get help on a function.

  

**Remember:**

  

- REPL is a powerful tool for learning, experimenting, and troubleshooting Python code.

- Take advantage of its interactive nature to explore Python's features and test your ideas quickly.

- If you need to create more complex programs or scripts, you'll still need to use Python files.