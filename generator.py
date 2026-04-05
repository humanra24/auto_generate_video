import random

def generate_script(idea):
    hooks = [
        "Did you know this?",
        "This will blow your mind!",
        "You won’t believe this!",
    ]

    hook = random.choice(hooks)

    script = f"""
    {hook}

    {idea}.

    Most people don't know this.

    This fact is absolutely amazing.

    Follow for more!
    """

    return script.strip()