import sys
import requests

def check_site(url: str):
    try:
        response = requests.get(url, timeout=5)
        print(f"Status: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python site_checker.py <url>")
        sys.exit(1)

    check_site(sys.argv[1])