import random

GREETINGS = [
    "Hallo",
    "Hi",
    "Guten Tag",
    "Servus",
    "Moin",
    "Grüß dich",
    "Hey",
    "Hallo zusammen",
]

def hallo(name: str = "Welt") -> str:
    """Gibt einen Begrüßungstext zurück."""
    return f"Hallo, {name}!"

def gruesse(name: str = "Welt") -> str:
    """Gibt eine zufällige Begrüßung zurück."""
    greeting = random.choice(GREETINGS)
    return f"{greeting}, {name}!"