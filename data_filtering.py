# Higher order functions for data filtering
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    # Filter using list comprehensions
    python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    adults = [worker["name"] for worker in DATA if worker["age"] > 18]
    old_people = [{**worker, **{"old": worker["age"] > 70}} for worker in DATA]

    print("Python developers: ")
    for worker in python_devs:
        print(worker)

    print("\nPlatzi workers")
    for worker in platzi_workers:
        print(worker)

    print("\nAdults")
    for worker in adults:
        print(worker)

    print("\nOld People")
    for worker in old_people:
        print(worker)

    # Filter using higher order 
    python_devs = list(filter(lambda worker: worker["language"] == "python",DATA))
    devs_names = list(map(lambda worker: worker["name"],python_devs))

    platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi",DATA))
    workers_names = list(map(lambda worker: worker["name"],platzi_workers))

    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults_names = list(map(lambda worker: worker["name"],adults))

    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    
    print("\nPython developers: ")
    for worker in devs_names:
        print(worker)

    print("\nPlatzi workers")
    for worker in workers_names:
        print(worker)
    
    print("\nAdults")
    for worker in adults_names:
        print(worker)

    print("\nOld People")
    for worker in old_people:
        print(worker)


if __name__ == '__main__':
    run()