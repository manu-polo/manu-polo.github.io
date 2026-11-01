people = []

with open("names.csv") as file:
    for line in file:
        name, city, age, car = line.rstrip().split(",")

        person = {
            "name": name,
            "city": city,
            "age": age,
            "car": car
        }

        people.append(person)


for person in people:
    print(f"{person['name']} is located in {person['city']}")
