import requests

url = "http://127.0.0.1:5000/bids"
data = {
    "user_id": 1,
    "item_id": 1,
    "bid_amount": 200
}

response = requests.post(url, json=data)
print("Response:", response.status_code)
print("Data:", response.json())
