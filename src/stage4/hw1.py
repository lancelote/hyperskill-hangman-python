SIMON = "Simon says"


def what_to_do(instructions: str) -> str:
    if instructions.startswith(SIMON):
        _, todo = instructions.split(SIMON)
        return f"I {todo.strip()}"
    elif instructions.endswith(SIMON):
        todo, _ = instructions.split(SIMON)
        return f"I {todo.strip()}"
    else:
        return "I won't do it!"
