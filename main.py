import json
import csv

if __name__ == "__main__":
    try:
        with open('data.json','r') as f:
            data = json.loads(f.read())


        output = '.'.join([*data[0]])
        for obj in data:
            output += f'\n{obj["name"]},{obj["age"]},{obj["mobile"]}'

        with open('output.csv','w') as f:
            f.write(output)

    except Exception as ex:
        print(f'Error:{str(ex)}')