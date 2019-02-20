import requests
from src import api_v1_consumer as apiv1


def build_complete_query(starting_index=0, batch_size=36):
    url = apiv1.base_url + apiv1.listings
    default_query_attributes = apiv1.default_request_attributes
    default_query_attributes["from"] = str(starting_index)
    default_query_attributes["size"] = str(batch_size)
    for key in default_query_attributes:
        url = url + str(key) + "=" + str(default_query_attributes[key]) + "&"
    return url[:-1]


def discover_available_items_from_api():
    url = build_complete_query()
    r = requests.get(url)
    json_obj = r.json()
    return json_obj['search']['totalCount'] + json_obj['developments']['search']['totalCount']


def obtain_id_price_and_area(listing):
    pricing_info = listing["pricingInfos"][-1]
    if (str(pricing_info['businessType']) == 'SALE') and (str(listing['showPrice']) == 'True'):
        unit_id = listing['id']
        unit_price = pricing_info['price']
        unit_usable_area = listing['usableAreas'][-1]
        return [str(unit_id), str(unit_price), str(unit_usable_area)]
    else:
        return [str(-1), str(0), str(0)]


def obtain_data_from_api():
    count = 0
    cursor_index = 0
    main_batch_size = 36

    total_count = discover_available_items_from_api()
    listings = []

    while count < total_count:
        query_url = build_complete_query(cursor_index, main_batch_size)
        r = requests.get(query_url)
        json_obj = r.json()

        for item in json_obj['developments']['search']['result']['listings']:
            observation = obtain_id_price_and_area(item['listing'])
            if observation[0] != "-1":
                listings = listings + [observation]
        for item in json_obj['search']['result']['listings']:
            observation = obtain_id_price_and_area(item['listing'])
            if observation[0] != "-1":
                listings = listings + [observation]

        count += main_batch_size
        cursor_index += main_batch_size
    return listings


def dump_data(filename, data):
    with open(filename, 'w') as output_file:
        for datum in data:
            output_file.write(str(datum) + "\n")


def main():
    filename = "vivareal_enseada_do_sua.txt"
    listings = obtain_data_from_api()
    dump_data(filename, listings)


if __name__ == "__main__":
    main()
