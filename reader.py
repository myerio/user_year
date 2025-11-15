def find_users_after(year):
    try:
        with open("users.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line or "," not in line:
                    continue  # skip empty or malformed lines
                name, birth_year = line.split(",")
                birth_year = int(birth_year)
                if birth_year > year:
                    print(name)
    except FileNotFoundError:
        print("Error: users.txt file not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the function
find_users_after(1996)