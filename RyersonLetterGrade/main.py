grade_ranges = {
    range(50, 56): 'D',
    range(56, 60): 'C-',
    range(60, 66): 'C',
    range(66, 70): 'C+',
    range(70, 76): 'B-',
    range(76, 80): 'B',
    range(80, 86): 'B+',
    range(86, 90): 'A-',
    range(90, 96): 'A',
    range(96, 100): 'A+',
}


def ryerson_letter(pct):
    if pct <= 50:
        return 'F'
    if pct >= 100:
        return 'A+'

    for grade_range, letter in grade_ranges.items():
        if pct in grade_range:
            return letter


if __name__ == '__main__':
    print(ryerson_letter(55))  
