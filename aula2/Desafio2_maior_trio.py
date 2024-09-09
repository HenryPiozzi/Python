N1 = int(input("Insira o primeiro numero "))
N2 = int(input("Insira o segundo numero "))
N3 = int(input("Insira o terceiro numero "))

if (N1 > N2):
    if(N1 > N3):
        print(f"O maior numero é {N1}")
    else:
        print(f"O maior numero é {N3}")
else:
    if ( N2 > N3):
        print(f"O maior numero é {N2}")
    else:
        print(f"O maior numero é {N3}")