cidade = str(input("Em qual cidade você nasceu? "))

cidade = cidade.split()

cidade[0] = cidade[0].upper()

verifica = "SANTO" in cidade[0]

print(f"{verifica}")