src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
anwser = [src[i + 1] for i in range(len(src) - 1) if src[i] < src[i + 1]]
print(anwser)
