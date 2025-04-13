# Internship
## Description
This project aims to extract lecture files from Moodle, preprocess them, and provide a search functionality using BERT embeddings. The project includes scripts to download files from Moodle, convert them to text, encode the text using BERT, and implement a search functionality through a Flask API. Additionally, a simple frontend interface allows users to interact with the search API.

## Installation
### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Moodle instance with necessary configurations

### Steps

1. Install required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. **Moodle Installation and Configuration**:
    - Ensure Moodle is installed and configured correctly on your server.
    - Upload sample lecture files to the Moodle courses.

2. **File Extraction**:
    - Run the `script.py` to extract lecture files from Moodle.
    ```bash
    python script.py
    ```

3. **Text Preprocessing**:
    - Run the `convert_pdf_to_text.py` to convert PDF files to text.
    ```bash
    python convert_pdf_to_text.py
    ```

4. **Embedding Text Data**:
    - Run the `encode.py` to encode text files using BERT and store embeddings.
    ```bash
    python encode.py
    ```

5. **Search Functionality**:
    - Run the `integrate.py` to start the Flask API.
    ```bash
    python integrate.py
    ```

6. **Frontend Interaction**:
    - Open `index.html` in a web browser to use the search interface.

## Scripts Description
- **`tokenizer.py`**: Loads the pre-trained BERT model and tokenizer.
- **`encode.py`**: Encodes text data using BERT and saves embeddings.
- **`search.py`**: Implements search functionality using BERT embeddings.
- **`integrate.py`**: Sets up a Flask API to handle search queries.
- **`script.py`**: Extracts lecture files from Moodle.
- **`convert_pdf_to_text.py`**: Converts extracted PDF files to text.
## Project Structure
Internship/
│
├── tokenizer.py
├── encode.py
├── search.py
├── integrate.py
├── script.py
├── convert_pdf_to_text.py
├── requirements.txt
├── text_files/
├── embeddings.json
├── README.md
└── index.html
## Features
- Extract lecture files from Moodle
- Convert PDF files to text
- Encode text using BERT embeddings
- Search functionality via Flask API

## Future Improvements
- Advanced search features (filtering, sorting)
- Fine-tuning BERT model for specific dataset
- Deployment on cloud platforms
- Enhanced user interface
- Scalability improvements

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
