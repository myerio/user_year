# reader.py

def read_users(file_path, year_threshold):
    with open(file_path, "r") as file:
        lines = file.readlines()
        result = []
        for line in lines:
            name, year = line.strip().split(",")
            if int(year) > year_threshold:
                result.append(name)
        return result

if __name__ == "__main__":
    users = read_users("users.txt", 1996)
    print(users)