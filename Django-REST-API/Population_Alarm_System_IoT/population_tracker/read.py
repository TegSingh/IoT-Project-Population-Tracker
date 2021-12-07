import requests

def main():

    r = requests.delete("https://www.tegveersingh.xyz:1880/sensor_data", data = {}, verify=False)
    print(r)

if __name__ == '__main__':
    main()