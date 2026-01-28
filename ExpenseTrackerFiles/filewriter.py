import json
import csv

class FileWriter:
    
    def write_json(self,report,total):
        file_path_json = "output.json"
        data = {
            "expenses": [
                {
                    "id": idx,
                    "Amount": e["amount"],
                    "Description": e["description"],
                    "Type": e["type"],
                }
                for idx, e in enumerate(report,1)
            ]
        }
        
        
        try:
            with open(file_path_json, 'w')as file:
                json.dump(data,file,indent=4)
        
            print(f"JSON file '{file_path_json}' has been created successfully")
        except FileExistsError:
            print("That file already exists.")

    def write_txt(self,report,total):
        file_path_txt = "output.txt"
        try:
            with open(file_path_txt, "w")as file:
                file.write("Id|Amount|Description|Credit/Debit\n")
                for idx, e in enumerate(report,1):
                    file.write(f"{idx}|{e['amount']}|{e['description']}|{e['type']}\n")
                file.write(f"Total Expenses were: {total}")
                print(f"txt file '{file_path_txt}' was created")
                
        except FileExistsError:
            print("That file already exists.")

    def write_csv(self,expense,total):
        file_path_csv = "output.csv"

        try:
            with open(file_path_csv, "w", newline='') as file:
                writer = csv.writer(file)

                writer.writerow(["Id", "Amount", "Description", "Type"])
                for idx, item in enumerate(expense, 1):
                    writer.writerow([idx,item["amount"], item["description"], item["type"]])

            print(f"CSV file '{file_path_csv}' has been created successfully")
        except FileExistsError:
            print("That file exists.")