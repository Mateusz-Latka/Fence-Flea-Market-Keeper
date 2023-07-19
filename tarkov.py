import requests

def run_query(query):
    response = requests.post('https://api.tarkov.dev/graphql', json={'query': query})
    response.raise_for_status()
    return response.json()

def get_item_data(name):
    query = f"""
    {{
        items(name: "{name}") {{
            name
            low24hPrice
            iconLink
            wikiLink
            width
            height
            changeLast48hPercent
            updated
        }}
    }}
    """

    try:
        result = run_query(query)
        items = result['data']['items']

        if not items:
            raise ValueError(f"Item '{name}' not found in the database.")

        item_data = items[0]
        return {
            'name': item_data['name'],
            'low24hPrice': item_data['low24hPrice'],
            'iconLink': item_data['iconLink'],
            'wikiLink': item_data['wikiLink'],
            'width': item_data['width'],
            'height': item_data['height'],
            'changeLast48hPercent': item_data['changeLast48hPercent'],
            'updated': item_data['updated']
        }
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to connect to the Tarkov API: {e}")
    except (KeyError, IndexError):
        raise Exception("Failed to parse the API response.")

def get_tier(search):
    if search >= 40000:
        return ':star:Legendary'
    elif search >= 30000:
        return ':green_circle:Great'
    elif search >= 20000:
        return ':yellow_circle:Average'
    elif search >= 10000:
        return ':red_circle:Poor'
    else:
        return ':x:Trash'  

def get_color(search):
    if search >= 40000:
        return 0xFF8C00
    elif search >= 30000:
        return 0x00FF00
    elif search >= 20000:
        return 0xFFFF66
    elif search >= 10000:
        return 0xFF0000
    else:
        return 0x800000