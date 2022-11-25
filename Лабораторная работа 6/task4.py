import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(file_name,delimiter: str = ',', new_line: str = '\n') -> list[dict]:
    dictionary = []
    with open(file_name) as file:
        name = next(file).strip(new_line).split(delimiter)

        for i in file:
            N = {data: coord for data, coord in zip(name, i.strip(new_line).split(delimiter))}
            dictionary.append(N)
    file.close()

    return dictionary


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

