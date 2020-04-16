import re
import requests
from requests.exceptions import RequestException

# Array of URLS that will be downloaded
urls = [
    '',
    '',
    '',
    #''
]

def main(x):

    try:
        with requests.get(x) as r:

            fname = ''
            if "Content-Disposition" in r.headers.keys():
                fname = re.findall("filename=(.+)", r.headers["Content-Disposition"])[0]
            else:
                fname = x.split("/")[-1]

            print(fname)
            open(fname, 'wb').write(r.content)

    except RequestException as e:
        print(e)


for i in range(len(urls)):
    print(urls[i])
    main(urls[i])