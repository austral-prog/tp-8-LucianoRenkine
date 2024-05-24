def get_coordinate(record):
    return record[1]

# print(get_coordinate(('Scrimshawed Whale Tooth', '2A'))) == 2A

def convert_coordinate(coordinate):
    return tuple(coordinate)

# print(convert_coordinate(get_coordinate(('Scrimshawed Whale Tooth', '2A')))) == ("2", "A")

def create_record(azara_record, rui_record):
    a = convert_coordinate(get_coordinate(azara_record))
    b = rui_record[1]
    if a == b:
        return azara_record + rui_record
    else:
        return "not a match"
