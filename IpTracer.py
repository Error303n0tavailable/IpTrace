import requests


def lookup_ip(ip):
    url = "https://deku-rest-api-ywad.onrender.com/iplu"
    params = {'ip': ip}

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            print("IP Lookup Results:")
            for key, value in data.items():
                print(f"{key}: {value}")
        else:
            print(f"Failed to lookup IP. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def main():
    ip = input("Enter the IP address: ")
    lookup_ip(ip)

if __name__ == "__main__":
    main()
