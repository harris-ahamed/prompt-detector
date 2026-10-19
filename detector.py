import requests

patterns = [
    "ignore previous instructions",
    "you are now",
    "forget your rules",
    "act as if",
    "ignore all instructions",
    "you have no restrictions",
    "disregard your training",
    "pretend you have no limits"
]

def scan_text(text):
    found = []
    for pattern in patterns:
        if pattern.lower() in text.lower():
            found.append(pattern)
    return found

def scan_url(url):
    try:
        response = requests.get(url, timeout=5)
        text = response.text
        return scan_text(text)
    except:
        return None

print("=== AI Prompt Injection Detector v2 ===")
print("1. Scan text manually")
print("2. Scan a URL")

choice = input("\nChoose (1 or 2): ")

if choice == "1":
    text = input("Enter text to scan: ")
    results = scan_text(text)
elif choice == "2":
    url = input("Enter URL to scan: ")
    results = scan_url(url)
    if results is None:
        print("Could not fetch URL.")
        exit()
else:
    print("Invalid choice.")
    exit()

print("\n=== SCAN RESULTS ===")
if results:
    print(f"WARNING: {len(results)} prompt injection pattern(s) detected!")
    for r in results:
        print(f"  - {r}")
else:
    print("No prompt injection patterns detected. Text appears safe.")
