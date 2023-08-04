
with open("data.txt") as file:
    data = [line.strip() for line in file.readlines()]
    file.close()

sector_id_sum = 0
north_pole_object_storage = None
alphas = "abcdefghijklmnopqrstuvwxyz"

def decrypt(slug, sec_id):
    ans = ""
    for i in slug:
        ans += alphas[(alphas.index(i) + sec_id) % 26]

    return ans

for seq in data:
    freq_set = {}
    letters = [i for i in set(seq) if i.isalpha()]
    checksum = seq[-6:-1]
    sector_id = int(seq.split('-')[-1].split('[')[0])

    for letter in letters:
        freq_set[letter] = seq.count(letter)

    code = list(freq_set.items())
    code.sort(key = lambda x: x[0])
    code.sort(key = lambda x: x[1], reverse = True)
    
    code = ''.join([i[0] for i in code])
    code = code[:5]

    if checksum == code:
        sector_id_sum += sector_id
        slugs = seq.split('-')[:-1]
        ans = ' '.join(decrypt(slug, sector_id) for slug in slugs)

        if 'north' in ans:
            north_pole_object_storage = sector_id

print(f"Part 1: {sector_id_sum}")
print(f"Part 2: {north_pole_object_storage}")
