#!/usr/bin/env python3
import requests
import csv
import json
from io import StringIO
from prettytable import PrettyTable
import os

class BINChecker:
    def __init__(self):
        self.db_url = "https://raw.githubusercontent.com/venelinkochev/bin-list-data/master/bin-list-data.csv"
        self.bin_data = self.fetch_database()
        self.results = []
    
    def check_bin(self, cc):
        T = PrettyTable()
        bin_number = cc[:6]
        
        if bin_number in self.bin_data:
            data = self.bin_data[bin_number]
            T.field_names = ['BIN', 'BRAND', 'TYPE', 'CATEGORY', 'ISSUER', 'COUNTRY']
            T.add_row([
                bin_number,
                data['brand'],
                data['type'],
                data['category'],
                data['issuer'],
                data['country']
            ])
            print(T)
            return True
        else:
            print(f"[+] BIN {bin_number} not found in database")
            return False

    def fetch_database(self):
        print("[+] Fetching BIN database...")
        bin_data = {}
        response = requests.get(self.db_url)
        if response.status_code == 200:
            csv_data = StringIO(response.text)
            reader = csv.DictReader(csv_data)
            for row in reader:
                bin_data[row['BIN']] = {
                    'brand': row.get('Brand', 'N/A'),
                    'type': row.get('Type', 'N/A'),
                    'category': row.get('Category', 'N/A'),
                    'issuer': row.get('Issuer', 'N/A'),
                    'issuer_phone': row.get('IssuerPhone', 'N/A'),
                    'issuer_url': row.get('IssuerUrl', 'N/A'),
                    'country': f"{row.get('CountryName', 'N/A')} ({row.get('isoCode2', 'N/A')})"
                }
            print(f"[+] Successfully loaded {len(bin_data)} BIN records")
        return bin_data

    def process_card_file(self, filename):
        print(f"[+] Processing cards from {filename}")
        T = PrettyTable()
        T.field_names = ['CARD', 'BRAND', 'TYPE', 'CATEGORY', 'ISSUER', 'COUNTRY']
        
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    card_data = line.split('|')
                    if len(card_data) >= 4:
                        card_number = card_data[0]
                        bin_number = card_number[:6]
                        expiry = f"{card_data[1]}/{card_data[2]}"
                        cvv = card_data[3]
                        
                        if bin_number in self.bin_data:
                            data = self.bin_data[bin_number]
                            T.add_row([
                                f"{card_number} ({expiry} | {cvv})",
                                data['brand'],
                                data['type'],
                                data['category'],
                                data['issuer'],
                                data['country']
                            ])
                            
                            # Store result for JSON
                            self.results.append({
                                'card_number': card_number,
                                'expiry': expiry,
                                'cvv': cvv,
                                'bin_data': data
                            })
        
        print(T)
        self.save_results()

    def save_results(self):
        output_file = 'bin_check_results.json'
        with open(output_file, 'w') as f:
            json.dump(self.results, f, indent=4)
        print(f"[+] Results saved to {output_file}")

def main():
    print("[+] Online BIN Checker v2.0")
    print("[+] Loading latest BIN database from GitHub")
    
    checker = BINChecker()
    
    while True:
        try:
            print("\n[1] Check single BIN")
            print("[2] Process cards.txt file")
            print("[3] Exit")
            
            choice = input("\n[•] Choose option > ")
            
            if choice == '1':
                cc = input("[•] ENTER FIRST 6 DIGITS OF CARD > ").strip().replace(" ", "")
                if len(cc) >= 6:
                    checker.check_bin(cc)
            elif choice == '2':
                if os.path.exists('cards.txt'):
                    checker.process_card_file('cards.txt')
                else:
                    print("[!] cards.txt not found!")
            elif choice == '3':
                print("[+] Thanks for using BIN Checker!")
                break
                
        except KeyboardInterrupt:
            print("\n[+] Thanks for using BIN Checker!")
            break
        except EOFError:
            print("\n[+] Thanks for using BIN Checker!")
            break

if __name__ == "__main__":
    main()
