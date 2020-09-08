def convert_to_int(integer_string_with_commas):
    if len(integer_string_with_commas) > 3 and "," not in integer_string_with_commas:
        return None
    comma_separated_parts = integer_string_with_commas.split(",")
    if not all([len(part) == 3 for part in comma_separated_parts]):
        return None
    integer_string_without_commas = "".join(comma_separated_parts)
    try:
        return integer_string_without_commas
    except ValueError:
        return None
