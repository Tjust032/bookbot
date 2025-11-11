def get_num_words(filepath):
    with open(filepath) as f:
        content = f.read()
        num_words = len(content.split())
        return num_words


def get_character_count(filepath: str):
    """
    Retrieves character count from book.

    Args:
        filepath (str): Path to book.

    Returns:
        dict: Dictionary of character counts
    """ 
    with open(filepath) as f:
        res = {}
        content = f.read()
        for char in content:
            char = char.lower()
            res[char] = res.get(char, 0) + 1
        return res

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    res = []
    for key, val in dict.items():
        res.append({"char": key, "num": val})
    res.sort(reverse=True, key=sort_on)
    return res
        