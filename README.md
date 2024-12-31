# BIN-VALIDATOR-CHECKER
BIN VALIDATION NO API REQUIRED. 6DIGIT BANK BIN VALIDATER AND CHECKER. I PROMISE THIS WORKS PERFECTLY


Here's a comprehensive README.md for the BIN Checker project:

# BIN Checker v2.0

A powerful Bank Identification Number (BIN) checking tool that validates card information using an extensive database.

## Features

- Real-time BIN database fetching from GitHub
- Single BIN lookup capability
- Batch processing of card lists
- Pretty table output format
- JSON export functionality
- User-friendly menu interface

## Installation

```bash
git clone https://github.com/noorali5780/BIN-VALIDATOR-CHECKER.git
cd bin-checker
pip install -r requirements.txt

Copy

Apply

README.md
Requirements
Python 3.x
requests
prettytable
Usage
Running the Tool

python BIN.py

Menu Options
Check single BIN
Process cards.txt file
Exit
Single BIN Check
Enter the first 6 digits of a card number to get detailed information including:

Brand
Type
Category
Issuer
Country
Batch Processing
Place your card list in cards.txt with the following format:

5458861506394502|02|2025|615
5459621515120101|08|2029|110

Copy

Apply

Format: CardNumber|ExpMonth|ExpYear|CVV

Output
Console Output
Results are displayed in a formatted table showing:

Card details
Brand information
Type
Category
Issuer details
Country information
JSON Export
Results are automatically saved to bin_check_results.json

Database Source
BIN database is sourced from: https://github.com/venelinkochev/bin-list-data

License
MIT License

Author
[SADIKI NOOR]


This README provides all necessary information for users to understand, install, and use the BIN Checker effectively.
