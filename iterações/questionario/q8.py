PA, PB, T1, T2 = input().split()
PA, PB = int(PA), int(PB)
T1, T2 = float(T1), float(T2)

anos = 0
alcançou = False

while PA <= PB and anos <= 1000:
    PA = int(PA * (1 + T1/100))
    PB = int(PB * (1 + T2/100))
    anos += 1

    if PA > PB:
        alcançou = True
        break

if alcançou:
    print(f"Vai alcancar em {anos} ano(s).")
elif anos > 1000:
    print(f"A nunca alcancara B.")
