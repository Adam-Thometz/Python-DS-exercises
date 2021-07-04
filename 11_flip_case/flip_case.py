def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    target_char = to_swap.lower()
    swapped_phrase = ''

    for char in phrase:
        if char.lower() == target_char:
            char = char.swapcase()
        swapped_phrase += char
    
    return swapped_phrase 