def get_lines(words, max_width):
    line, lines = [], []
    line_count, char_count = 0, 0

    for word in words:
        word_len = len(word)
        if line_count + word_len > max_width:
            lines.append([line, char_count])
            line_count, char_count = 0, 0
            line = []
        line.append(word)
        line_count += word_len + 1
        char_count += word_len

    if line:
        lines.append([line, char_count])

    return lines


def full_justify(words, max_width):
    lines = get_lines(words, max_width)
    last_line = len(lines) - 1
    justified_lines = []

    for index, (line, char_count) in enumerate(lines):
        spaces = max_width - char_count

        if index == last_line or len(line) == 1:
            juststr = " ".join(line).ljust(max_width, ' ')
            justified_lines.append(juststr)
        else:
            if spaces % (len(line) - 1) == 0:
                pad = " " * (spaces // (len(line) - 1))
                juststr = pad.join(line)
                justified_lines.append(juststr)
            else:
                quot, rem = divmod(spaces, len(line) - 1)
                pads = [quot] * (len(line) - 1)

                # Distribute excess spaces starting from LHS
                for i in range(rem):
                    pads[i] += 1

                for index, pad in enumerate(pads):
                    line[index] = ''.join([line[index], ' '*pad])

                justified_lines.append(''.join(line))

    return justified_lines


if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    max_width = 16
    result = full_justify(words, max_width)
    print(f'result {result}')
