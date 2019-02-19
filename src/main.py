import requests
from src import api_v1_consumer as apiv1


def build_complete_query(batch_size=1):
    url = apiv1.base_url + apiv1.listings
    default_query_attributes = apiv1.default_request_attributes
    default_query_attributes["size"] = batch_size
    print("Corrected size = " + str(default_query_attributes["size"]))
    for key in default_query_attributes:
        url = url + str(key) + "=" + str(default_query_attributes[key]) + "&"
    return url[:-1]


def discover_available_items_from_api():
    url = build_complete_query()
    r = requests.get(url)
    json_obj = r.json()
    return json_obj['search']['totalCount']


def obtain_data_from_api():
    #total_count = discover_available_items_from_api()
    total_count = 36 #discover_available_items_from_api()
    huge_url = build_complete_query(total_count)
    r = requests.get(huge_url)
    json_obj = r.json()

    i = 1
    for value in json_obj['search']['result']['listings']:
        print(value)
        print(i)
        i = i+1


def main():
    obtain_data_from_api()


if __name__ == "__main__":
    main()
