# convención de nombres en Python llamada PEP 8, que define cómo se deben escribir los nombres según lo que representen.

# Resumen rápido:
# Tipo de cosa	            Convención de nombres	        Ejemplo correcto
# Clases	                PascalCase o CamelCase	        CharacterManager
# Funciones o variables	    snake_case	                    character_manager

# ¿Qué es OOP (Programación Orientada a Objetos)?
# OOP significa Object-Oriented Programming (Programación Orientada a Objetos).
# Es una forma de organizar tu código basada en objetos que tienen:
# Propiedades (también llamadas atributos o datos).
# Acciones (también llamadas métodos o funciones que puede hacer ese objeto).
# Es como modelar cosas del mundo real: personas, autos, tareas, personajes, etc.

# ¿Qué es class en Python?
# Una clase (class) es como un molde o plantilla que usamos para crear objetos.
# Piensa en una receta para hacer galletas. La receta no es una galleta, pero puedes usarla para hacer muchas galletas. Lo mismo pasa con las clases.


# Esta clase tiene:

# Atributos:
# self.characters: una lista de personajes.
# self.next_id: el próximo ID a asignar.

# Métodos (acciones que puede hacer el manager):
# get_all(): devolver todos los personajes.
# get(id): buscar uno por ID.
# create(data): crear uno nuevo.
# update(id, data): actualizar uno.
# delete(id): eliminar uno.

class CharacterManager:
    # Es una plantilla de Python (una clase) que usamos para organizar la lógica del CRUD de personajes.
    # Todo lo que tenga que ver con agregar, buscar, editar o borrar personajes está dentro de esta clase.

    # Es como una caja de herramientas para manejar personajes.


    def __init__(self):

        # Esto es lo que se llama un constructor.

        # Se ejecuta automáticamente cuando creamos un nuevo CharacterManager.

        # Sirve para preparar las cosas que necesitaremos dentro del objeto (por ejemplo, la lista de personajes).


        self._characters = [
            # En Python, no existe encapsulamiento forzado como en otros lenguajes, pero se simula usando guiones bajos.
            # Esto es una convención que le dice a otros programadores:

            # “¡Ey! Esto es interno, no lo toques directamente.”

            # Pero sigue siendo accesible si alguien quiere (aunque no debería).
            {
                'id': 1,
                'name': 'Gandalf',
                'quote': 'A wizard is never late, nor is he early. He arrives precisely when he means to.'
            },
            {
                'id': 2,
                'name': 'Frodo Baggins',
                'quote': 'I will take the Ring to Mordor. Though… I do not know the way.'
            },
        ]
        self._next_id = 3

        # Significa: la lista de personajes que le pertenece a este CharacterManager en particular.

        # Si no usáramos self, estaríamos usando variables sueltas que se pierden fuera de la clase.

    def get_all(self):
        return self._characters

    def get(self, char_id):
        for character in self._characters:
            if character["id"] == char_id:
                return character
        return None

    def create(self, data):
        character = {
            "id": self._next_id,
            "name": data["name"],
            "quote": data["quote"]
        }
        self._characters.append(character)
        self._next_id += 1
        return character

    def update(self, char_id, data):
        #Podemos reutilizar el metodo get para obtener el character
        character = self.get(char_id)
        if character:
            character["name"] = data.get("name", character["name"])
            character["quote"] = data.get("quote", character["quote"])
        return character

    def delete(self, char_id):
        #Podemos reutilizar el metodo get para obtener el character
        character = self.get(char_id)
        if character: 
            self._characters.remove(character)
            return True
        return False