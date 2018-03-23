


def center(string, length, pad_char= ' '):
    """Put @string in the middle of a @lenght-long sequence of @pad_char,
    truncating it if necessary."""
    return string[:length].center(length,pad_char)