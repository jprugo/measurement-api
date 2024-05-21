from typing import List
import csv

def write_to_csv(data: List[object], filename: str):
    if data:
        data = list(map(lambda o: o.__dict__, data))
        fieldnames = data[0].keys()
        with open(filename, mode='w', newline='') as archivo_csv:
            writer = csv.DictWriter(archivo_csv, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)