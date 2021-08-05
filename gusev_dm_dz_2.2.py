text = ['в', '"', '5', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+5', '"', 'градусов']
new_text = []
for i in text:
    if i.isdigit():
        num = int(i)
        new_text.extend([f'{num:02d}'])
    elif i.startswith('-') or i.startswith('+') and i[1:].isdigit():
        num = int(i[1:])
        new_text.extend([f'{i[0]}{num:02d}'])
    else:
        new_text.append(i)
txt = ' '.join(new_text)
print(txt)
