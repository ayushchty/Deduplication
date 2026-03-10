# Deduplication

A Python-based data deduplication tool that helps identify and remove duplicate records from CSV and other file formats using fuzzy string matching.

## Features

- **Web Interface**: Easy-to-use Flask-based web application for uploading files and removing duplicates
- **CLI Interface**: Command-line tool for batch processing
- **Fuzzy Matching**: Uses fuzzy string matching (80% similarity threshold) to detect similar/duplicate entries
- **Multiple Format Support**: Supports CSV, Excel, JSON, and TXT files
- **Database Integration**: MySQL database support for deduplication
- **Docker Support**: Containerized deployment option

## Installation

### Prerequisites

- Python 3.x
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd Deduplication
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Web Application

Run the Flask application:
```bash
python app.py
```

The web interface will be available at `http://localhost:5000`

1. Upload a CSV file through the web interface
2. The system will identify duplicate records using fuzzy matching
3. Download the cleaned file with duplicates removed

### Command Line Interface

Run the CLI version:
```bash
python main.py
```

Follow the prompts to:
1. Enter the file path
2. View duplicate records
3. Remove duplicates if desired
4. Save the modified file

## Docker

### Build the Docker image:
```bash
docker build -t dedupe .
```

### Run the container:
```bash
docker run -it --rm --name my-running-app dedupe
```

## Dependencies

- Flask==3.1.0
- pandas==2.2.3
- fuzzywuzzy==0.18.0
- python-Levenshtein (for fuzzywuzzy performance)

See `requirements.txt` for complete list.

## How It Works

The deduplication process uses fuzzy string matching algorithm:

1. **File Loading**: Reads the input file (CSV, Excel, JSON, etc.)
2. **Fuzzy Matching**: Compares string values across all text columns using fuzzy matching with 80% similarity threshold
3. **Standardization**: Replaces similar strings with a canonical form
4. **Deduplication**: Removes exact duplicate rows
5. **Export**: Saves the cleaned data to a new file

## License

MIT License

