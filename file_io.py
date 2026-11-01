people = []

with open("names.csv") as file:
    for line in file:
        name, city, age, car = line.rstrip().split(",")
        person = {"name": name, "city": city, "age": age, "car": car}
        people.append(person)


output = ""

for person in people:
    output += f"""
        <p>
            {person['name']} is located in {person['city']}
        </p>
    """


with open("index.html") as file:
    html = file.read()

html = html.replace("{{ PYTHON_OUTPUT }}", output)

with open("index.html", "w") as file:
    file.write(html)
