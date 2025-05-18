import gspread
from google.oauth2.service_account import Credentials
from flask import Flask, request

# Google API hitelesítés
scope = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("service_account.json", scopes=scope)
client = gspread.authorize(creds)

# Google Sheet elérése
sheet_id = "1a1ykYHv7S1e77F6ROWk8Ix2UHdrLqZazlwKOUVpBVO0"
spreadsheet = client.open_by_key(sheet_id)
sheet = spreadsheet.worksheet("Új jelentkezések")

# Flask app
app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()  # ha nem JSON, akkor: request.form.to_dict()
    print("Érkezett adat:", data)

    # Mezők lekérése (ha valamelyik nincs, legyen üres string)
    row = [
        data.get("Időpont", ""),
        data.get("Név", ""),
        data.get("Email", ""),
        data.get("Telefon", ""),
        data.get("Lakhely", ""),
        data.get("Kor", ""),
        data.get("Képességeim, ismereteim", ""),
        data.get("Napszakok", ""),
        data.get("Megjegyzés", "")
    ]

    # Új sor hozzáadása
    sheet.append_row(row)

    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)