"""Compito 1 (https://github.com/Enkkfull/hard-python/blob/main/lezione3/compiti/compiti.md)"""

def inputs_list():
    """
    Get a sequence of words or punctuation symbols as input and return them in a list.
    To terminate the sequence write "stop".

    Returns:
        List of strings.
    """

    inputs = []
    input_string = ""

    print("Inserire serie di parole/simboli di punteggiatura:")
    while input_string != "stop":
        input_string = input()
        inputs.append(input_string)

    inputs.remove("stop")

    return inputs


def is_terminator(string):
    """Determine if given string is ".", "!" or "?".

    Arguments:
        string -- tested string.

    Returns:
        Boolean value.
    """

    return string in (".", "!", "?")


def build_text(strings):
    """Build text from a list of strings.

    Arguments:
        strings -- list of words or punctuation symbols.

    Returns:
        String of text.
    """

    text = ""

    strings[0] = strings[0].capitalize()
    for i, string in enumerate(strings):
        if is_terminator(string):
            strings[i + 1] = strings[i + 1].capitalize()

    text = " ".join(strings)

    terminators = (".", "!", "?")
    for terminator in terminators:
        text = text.replace(f" {terminator} ", f"{terminator}\n")

    return text.replace(" ,", ",")


def punctuation_count(text):
    """Count number of punctuations symbols in a text.

    Arguments:
        text -- string to count.

    Returns:
        Number of punctuation symbols.
    """

    count = 0

    for char in text:
        if is_terminator(char) or char == ",":
            count += 1

    return count


def characters_counts(text):
    """Build a dictionary containing the count of every character in the text.

    Arguments:
        text -- string to check.

    Returns:
        Dictionary in the form "character": count.
    """

    counts = {}

    for char in text:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1

    counts.pop(" ")
    counts.pop("\n")

    return counts


def most_frequent_char(text):
    """Finds most frequent character in text.

    Arguments:
        text -- string to check.

    Returns:
        String.
    """

    counts = characters_counts(text)
    most_frequent = list(counts.keys())[0]
    most_frequent_count = counts[most_frequent]

    for key, value in characters_counts(text).items():
        if value > most_frequent_count:
            most_frequent = key
            most_frequent_count = value

    return most_frequent


def least_frequent_char(text):
    """Find least frequent character in text.

    Arguments:
        text -- string to check.

    Returns:
        String.
    """

    counts = characters_counts(text)
    least_frequent = list(counts.keys())[0]
    least_frequent_count = counts[least_frequent]

    for key, value in characters_counts(text).items():
        if value < least_frequent_count:
            least_frequent = key
            least_frequent_count = value

    return least_frequent


def main():
    """Main method"""

    text = build_text(inputs_list())

    print("\nTesto:", text, sep="\n", end="\n\n")
    print("Numero parole:", len(text.split()))
    print("Numero simboli punteggiatura:", punctuation_count(text))
    print("Numero frasi:", len(text.split("\n")))
    print("Carattere più frequnte:", most_frequent_char(text))
    print("Carattere meno frequente:", least_frequent_char(text))


if __name__ == "__main__":
    main()
