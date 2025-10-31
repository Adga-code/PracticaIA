from src.database import connect
from random import choice, randint  #! INVESTIGAR CHOICE

def respond_to_input(user_input):
    response = {1:1, 2:2, 3:3, 4:4, 5:5}  # Example response mapping
    # Example function to process user input
    data = connect.getSome(connect.getCollection("datosBasicos"), {"input": user_input})

    choices = [item['output'] for item in data]
    if choices:
        return choice(choices)
    else:
        return "No valid response found."


def train_model(ia_input, user_output):
    # Example function to train a model
    data = {"output": user_output, "input": ia_input}
    connect.insert(connect.getCollection("entrenamiento"), data)
