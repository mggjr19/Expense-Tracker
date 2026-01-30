import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

class APIretriever:

    
    def __init__(self,token = None):
        self.token = token
        self.url = (
    "https://api.stlouisfed.org/fred/series/observations" + \
    "?series_id={seriesID}&api_key={key}&file_type=json" + \
    "&observation_start={start}&observation_end={end}&units={units}"
)

    def set_token(self,token):
        self.token = token

    def get_series(self, series_id, start, end, units):
        url_formatted = self.url.format(
            seriesID = series_id, start = start, end = end, units = units, key = self.token
        )

        response = requests.get(url_formatted)
        data = response.json()
        data = data["observations"][0]["value"]

        return data
    
    def create_print_data(self,total,food,housing,transportation):
        
        #reading the api key so we can get data from FRED API
        with open('secrets_keys.json', 'r')as f:
            secrets = json.load(f)
        api_key = secrets["api_key"]
        self.set_token(api_key)

        categories = {
            "Total Average Annual Expenditures": total,
            "Food": food,
            "Housing": housing,
            "Transportation": transportation,
        }       

        rows = []
        for name, series_id in categories.items():
            value = self.get_series(
            series_id=series_id,
            start="2024-01-01",
            end="2024-01-01",
            units="lin"
        )
            rows.append({
            "Name": name,
            "Period": 2024,
            "Value": value
            })

        df = pd.DataFrame(rows)
        print(df.to_string(index=False))

        return


    def define_bracket(self,income):

        print("For your income bracket, this is how much people spend(): ")
        print("(Brackets are divided into 5 sub categories for every 20th percentile)")

        if income <= 16658:
            self.create_print_data("CXUTOTALEXPLB0102M","CXUFOODTOTLLB0102M","CXUHOUSINGLB0102M","CXUTRANSLB0102M")
        elif income <= 42925:
            self.create_print_data("CXUTOTALEXPLB0103M","CXUFOODTOTLLB0103M","CXUHOUSINGLB0103M","CXUTRANSLB0103M")
        elif income <= 74474:
            self.create_print_data("CXUTOTALEXPLB0104M","CXUFOODTOTLLB0104M","CXUHOUSINGLB0104M","CXUTRANSLB0104M")       
        elif income <= 121548:
            self.create_print_data("CXUTOTALEXPLB0105M","CXUFOODTOTLLB0105M","CXUHOUSINGLB0105M","CXUTRANSLB0105M")
        else:
            self.create_print_data("CXUTOTALEXPLB0106M","CXUFOODTOTLLB0106M","CXUHOUSINGLB0106M","CXUTRANSLB0106M")
        
        return

