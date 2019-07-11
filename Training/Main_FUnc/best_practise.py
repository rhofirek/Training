from time import sleep

print("This is my file to demonstrate best practices")

def process_data(data):
    print ("beginning data processing ...")
    modifie_data= data + " that has been modified"
    sleep(3)
    print("Data processing finished")
    return modifie_data

def read_data_from_Web():
    print("Reading data from web")
    data = "Data from web"
    return data

def write_data_to_db(data):
    print("writing data to database")
    print(data)


def main():
    data = read_data_from_Web()
    modified_data = process_data(data)
    write_data_to_db(modified_data)

if __name__ == "__main__":
    main()