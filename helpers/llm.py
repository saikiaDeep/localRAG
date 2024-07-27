import requests

def call_llm(prompt):
        
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama2",
        "prompt": prompt,
        "stream": False
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")
    # data = response.json()
    # print(data.get('response'))
    return response.json()