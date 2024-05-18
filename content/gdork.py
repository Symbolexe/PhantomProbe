#!/usr/bin/python3
import sys
from googlesearch import search

def google_search(domain):
    search_query = f"site:*.{domain}"
    try:
        search_results = search(search_query, num=100, stop=100, pause=2)
        for i, result in enumerate(search_results, start=1):
            print(f"{i}. {result}")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Example Usage: python3 CortexLink-GDork.py google.com")
        sys.exit(1)
    
    target_domain = sys.argv[1]
    google_search(target_domain)
