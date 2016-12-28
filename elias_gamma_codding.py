from base_numeral_system import base_ns


def encode_word(item):
    code = base_ns.convert(item, 2).integer
    return ((len(code) - 1) * [0]) + code


def encode(data: list):
    # Encode phrase
    result = []
    for item in data:
        result += encode_word(item)
    return result


def decode(k: list):
    k = k[:]
    result = []

    n = 1
    while len(k) > 0:
        a = k[:1]
        k = k[1:]

        if a == [0]:
            n += 1
        else:
            a += k[:n-1]
            k = k[n-1:]
            result.append(int(base_ns.convert_to_dec(base_ns.NumberBased(2, a))))
            n = 1

    return result
