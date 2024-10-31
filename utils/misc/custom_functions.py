from data.translation import to_cyrillic


# Faylni transliteratsiya qiluvchi funksiyasi
def transliterate_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Har bir qatorni transliteratsiya qilib, yangi faylga yozamiz
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in lines:
            transliterated_line = to_cyrillic(line)
            f.write(transliterated_line)
