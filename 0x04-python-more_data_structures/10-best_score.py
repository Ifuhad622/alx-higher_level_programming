#!/usr/bin/python3
# 10-best_score.py


def best_score(a_dictionary):
    """Return key with biggest integer value."""
    return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None
