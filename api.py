import requests
import json
import blaze_double


def double():
    url = requests.get('http://127.0.0.1:65000/blaze/double')
    data = json.loads(url.content)
    results = data["blaze_double"]["results"]
    return results


check_double = []
while True:
    results_double = double()

    if results_double != check_double:
        print(results_double)
        check_double = results_double
        blaze_double.estrategy(results_double)
