# Readme Generator powered by OpenAI

## Description
The Readme Generator is a Streamlit-based web application designed to help you create professional README.md files effortlessly. It leverages OpenAI's GPT model to analyze the provided code snippets and generate well-structured and detailed README.md files in Markdown format. The application offers a user-friendly interface where users can upload their code files and obtain a fully formatted README.

## Installation Instructions

To use the Readme Generator, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/readme-generator.git
   cd readme-generator
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `secrets.json` file in the root directory of the project and add your OpenAI API key in the following format:
   ```json
   {
       "api_key": "YOUR_OPENAI_API_KEY"
   }
   ```

## Usage

To start the application, run:
```bash
streamlit run app.py
```

### Steps to Generate README:

1. Open your web browser and navigate to `http://localhost:8501`.
2. Upload the code files for which you want to generate a README.md file by clicking on "Browse files" or drag and drop the files.
3. Click the "Generate README" button.
4. If no files are uploaded, a warning message will appear prompting you to upload your code files.
5. Once the README.md content is generated, it will be displayed in two columns:
   - **Your Readme:** Shows the raw Markdown code of the generated README.
   - **Preview:** Displays the rendered Markdown so you can see how it looks.

## Examples

### Example Input

Uploading a single Python file with the following content:
```python
import numpy as np

def add(a, b):
    return np.add(a, b)

def subtract(a, b):
    return np.subtract(a, b)
```

### Example Output

```markdown
# Project Title

## Description
This project deals with basic arithmetic operations using numpy. It includes functionalities to add and subtract two numbers.

## Installation Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/project.git
   cd project
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To use the arithmetic operations, you can import the functions from the script and call them as follows:
```python
from your_module import add, subtract

result_add = add(1, 2)
result_subtract = subtract(2, 1)
print(f"Addition Result: {result_add}")
print(f"Subtraction Result: {result_subtract}")
```

## License
This project is licensed under the MIT License.
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---

Feel free to contribute to the project by submitting pull requests or reporting issues.

## Acknowledgments
This project makes use of [Streamlit](https://streamlit.io) for the web interface and [OpenAI](https://openai.com) for the AI-based README generation.

## Contact
For any inquiries or support, please contact [yourname@example.com](mailto:yourname@example.com).

---

**Note:** This application assumes that you have valid access to OpenAI's GPT model API. Ensure your API key is stored securely and do not share it publicly.