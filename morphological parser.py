def morphological_parser(word):
    # Define a dictionary of suffixes and their meanings
    suffix_rules = {
        "ing": "Present participle or gerund",
        "ed": "Past tense",
        "s": "Plural or third-person singular",
        "er": "Agent or comparative",
        "est": "Superlative",
        "ly": "Adverb",
        "ness": "State of being",
        "un": "Negation (prefix)",  # Exception: check for prefixes
        "re": "Repetition or backward (prefix)",  # Prefix example
    }

    # Results to store parsing information
    result = {"root": None, "affixes": []}

    # Check for prefixes
    for prefix in ["un", "re"]:
        if word.startswith(prefix):
            result["affixes"].append({"affix": prefix, "type": "prefix", "meaning": suffix_rules[prefix]})
            word = word[len(prefix):]  # Remove prefix for further analysis

    # Check for suffixes
    for suffix in sorted(suffix_rules.keys(), key=len, reverse=True):  # Longest suffix first
        if word.endswith(suffix) and suffix not in ["un", "re"]:  # Ignore prefixes here
            result["affixes"].append({"affix": suffix, "type": "suffix", "meaning": suffix_rules[suffix]})
            word = word[:-len(suffix)]  # Remove suffix for further analysis

    # Assign the remaining part as the root
    result["root"] = word if word else "Unknown"

    return result

# Example Usage
words = ["unhappiest", "redoing", "walked", "teachers", "happily", "sadness"]

for word in words:
    print(f"Word: {word}")
    print(morphological_parser(word))
    print()
