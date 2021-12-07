import requests


def main():

    id = input("Enter ID: ")
    distance = input("Enter Distance: ")

    parameters = {"id" : id , "distance": distance}

    r = requests.post("https://www.tegveersingh.xyz:1880/add", data = parameters, verify=False)
    print(r.url)

if __name__ == '__main__':
    main()