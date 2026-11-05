import requests

BASE = "http://127.0.0.1:5001"

r = requests.get(f"{BASE}/")
print("GET /:", r.status_code, r.json())
assert r.status_code == 200

r = requests.get(f"{BASE}/hello")
print("GET /hello:", r.status_code, r.json())
assert r.status_code == 200 and "message" in r.json()

r = requests.get(f"{BASE}/data")
print("GET /data:", r.status_code, r.json())
assert r.status_code == 200 and isinstance(r.json(), list)

r = requests.post(f"{BASE}/data", json={"name": "Monitor", "price": 199})
print("POST /data:", r.status_code, r.json())
assert r.status_code == 201 and r.json()["price"] == 199

r = requests.post(f"{BASE}/data", json={})
print("POST /data (bad):", r.status_code, r.json())
assert r.status_code == 400

print("All tests passed ✅")