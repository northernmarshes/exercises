#!/usr/bin/env python3
# Zadanie 3: Podziel listę na 3 równe części i odwróć każdą część

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

def sliceit(numbers):
    """creates 3 reversed chunks"""
    chunk_no = len(numbers) // 3
    chunks = []
    result = []
    for i in range(0,len(numbers), chunk_no):
        cut = slice(i,i+3)
        chunk = numbers[cut]
        chunk.reverse()
        chunks.append(chunk)
    return chunks

sliceit(sample_list)

# ----------- Future Tips: -----------
# powinno być slice(i,i+chunk_no)
# nie mutować oryginalnych danych!
# nazwa chunk_no może być myląca
