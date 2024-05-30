import os
file_path = 'in.ernet.dli.2015.378636/2015.378636.apne-isii_djvu.txt'
def extract_paragraphs(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    total_lines = len(lines)

    first_paragraph = ""
    for line in lines:
        if line.strip():  
            first_paragraph += line
        else:
            break  

    #middle paragraph
    middle_line_index = total_lines // 2
    middle_paragraph = ""
    i = middle_line_index

    #start of mid para
    while i >= 0 and not lines[i].strip():
        i -= 1
    while i >= 0 and lines[i].strip():
        middle_paragraph = lines[i] + middle_paragraph
        i -= 1

    #end of mid para
    i = middle_line_index + 1
    while i < total_lines and not lines[i].strip():
        i += 1
    while i < total_lines and lines[i].strip():
        middle_paragraph += lines[i]
        i += 1

    #last paragraph
    last_paragraph = ""
    i = total_lines - 1
    while i >= 0 and not lines[i].strip():
        i -= 1
    while i >= 0 and lines[i].strip():
        last_paragraph = lines[i] + last_paragraph
        i -= 1

    return first_paragraph, middle_paragraph, last_paragraph

first, middle, last = extract_paragraphs(file_path)

print("First Paragraph:")
print(first)

print("\nMiddle Paragraph:")
print(middle)

print("\nLast Paragraph:")
print(last)
