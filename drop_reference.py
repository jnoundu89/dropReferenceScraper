import requests
import pandas as pd


def dropreference_components(component_type,component_model):
    payload = {
        "filter": {
            "models": [
                f"{component_model}"
            ]
        },
        "page": 0
    }
    page = requests.post(f'https://api-dropreference.com/drops/FR/{component_type}', json=payload)
    if page.status_code == 200:
        df = pd.json_normalize(page.json()['drops'])
        s_component_model = component_model.replace(" ", "_")
        df.to_csv(f"{component_type}_{s_component_model}.csv", index=False)