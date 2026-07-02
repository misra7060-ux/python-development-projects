import requests

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=3"

try:
    data = requests.get(url)
    print("\nWeather Report")
    print(data.text)
except:
    print("Something went wrong!")