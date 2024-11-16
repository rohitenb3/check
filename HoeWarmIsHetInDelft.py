import requests
from bs4 import BeautifulSoup

def get_temperature():
    try:
        # Request the weather page
        response = requests.get("http://www.weerindelft.nl/")
        response.raise_for_status()  # Check if the request was successful

        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the temperature on the page (HTML structure may vary, so adjust as needed)
        temperature_tag = soup.find("div", class_="temperature")  # Adjust class name accordingly
        temperature_text = temperature_tag.get_text(strip=True)

        # Extract and round temperature
        temperature = round(float(temperature_text.split()[0]))  # Extract the numeric value

        print(f"{temperature} degrees Celsius")

    except Exception as e:
        print("Error retrieving temperature:", e)

if __name__ == "__main__":
    get_temperature()