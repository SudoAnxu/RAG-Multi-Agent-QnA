import requests

def calculator(expr):
    import math
    allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    try:
        return f"Result: {eval(expr, {'__builtins__':None}, allowed_names)}"
    except Exception as e:
        return f"Error in calculation: {e}"

def dictionary_lookup(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            defs = resp.json()[0]['meanings'][0]['definitions'][0]['definition']
            return f"{word}: {defs}"
        else:
            return f"Word not found: {word}"
    except Exception as e:
        return f"Error: {e}"