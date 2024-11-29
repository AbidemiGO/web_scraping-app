import requests
import selectorlib
import time
from datetime import datetime


url = "https://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    """scrape the page source from the url
    """
    response = requests.get(url, headers= HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def store(extracted):
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    with open("data.txt", "a") as file:
        line = f"{now}, {extracted}\n"
        file.write(line)


# def read(extracted):
    # with open("data.txt", "r") as file:
        # return file.read()


if __name__ == "__main__":
    scraped = scrape(url)
    extracted = extract(scraped)
    print(extracted)
    store(extracted)



        # content = read(extracted)
        # if extracted != "No upcoming tours":
            # if extracted not in content:
                # store(extracted)
                # send_mail()
        # time.sleep(2)


