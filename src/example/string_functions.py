"""Some example string functions."""


def give_greetings(name: str, greeting: str = "Hello {name}!") -> str:
    """
    Greet a person.
    :param name: Name of person which shall be greeted
    :param greeting: The way to greet
    :return: Personalized greetings
    """
    return greeting.format(name=name)
