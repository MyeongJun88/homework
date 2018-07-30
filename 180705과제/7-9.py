def krw_to_usd(won):
    return won / 1000

def usd_to_jpy(dollars):
    return dollars*125

amounts = [1000, 2000, 3000, 5000, 8000, 13000, 21000, 34000]

print("한국 화폐: " + str(amounts))

i=0
while i < len(amounts):
    amounts[i] = krw_to_usd(amounts[i])
    i += 1

print("미국 화폐: " + str(amounts))

i=0
while i < len(amounts):
    amounts[i] = usd_to_jpy(amounts[i])
    i += 1

print("일본 화폐: " + str(amounts))