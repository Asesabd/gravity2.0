import requests

url = "https://gravity2-0.onrender.com/webhook"  # ← Ezt cseréld ki, ha nem ez az endpoint!

adat = {
    "name": "Teszt Elek",
    "email": "teszt@valami.hu",
    "message": "Ez egy próbabejegyzés Pythonból"
}

response = requests.post(url, json=adat)

print("Státuszkód:", response.status_code)
print("Válasz:", response.text)