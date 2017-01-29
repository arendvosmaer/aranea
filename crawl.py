import requests
import config
import db

def fetchCase(baseurl, ecli):
    result = requests.get(baseurl + ecli)
    return result

def main():
    # result = fetchCase(config.baseurl, config.example_ecli)
    # print(result.text)
    print(db.makeQueue())

if __name__ == "__main__":
    main()
