import json


class FileWriter:
    
    def write_json(self,expense):
        file_path_json = "output.json"
        try:
            with open(file_path_json, 'w')as file:
                json.dump(expense,file,ident=4)
        
            print(f"JSON file '{file_path_json}' has been created successfully")
        except FileExistsError:
            print("That file already exists!")

    def write_txt(self,expense):
        file_path_txt = "output.txt"
        try:
            with open(file_path_txt, "w")as file:
                file.write("Amount|Description|Credit/Debit|Frequency\n")
                for e in expense:
                    file.write(f"{e['amount']}|{e['description']}|{e['type']}|{e['frequency']}")
                print(f"txt file '{file_path_txt}' was created")
        except FileExistsError:
            print("That file already")
