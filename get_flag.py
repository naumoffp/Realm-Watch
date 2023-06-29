import os
import sys
import webbrowser

def get_flag_filename(country, size):
    for file in os.listdir():
        if file.startswith(f"icons8-{country.lower().replace(' ', '-')}-"):
            if f"{size}." in file:
                return file
    return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py [country] [size]")
        sys.exit(1)

    country = sys.argv[1]
    size = sys.argv[2]

    filename = get_flag_filename(country, size)
    if filename:
        url = f"file://{os.path.abspath(filename)}"
        webbrowser.get("chrome").open(url)
    else:
        print(f"No flag found for {country} with size {size}.")
