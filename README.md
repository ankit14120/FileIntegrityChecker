# File Integrity Checker

A beginner cybersecurity project built with Python.

## Features

- Generate SHA-256 hashes
- Register files
- Detect file modifications
- Store hashes in JSON

## Requirements

- Python 3.10+
- colorama

## Installation

pip install -r requirements.txt

## Run

python main.py

## Project Structure

-- FileIntegrityChecker/
 - │
 - ├── main.py
 - ├── sample.txt
 - ├── image.png
 - ├── report.pdf
 - ├── hashes/
 - │   ├── sample_hash.txt
 - │   ├── image_hash.txt
 - │   └── report_hash.txt
 - ├── README.md
 - └── requirements.txt

## Example

Register a file:

sample.txt

Verify the file.

If the file changes, the program detects it.
