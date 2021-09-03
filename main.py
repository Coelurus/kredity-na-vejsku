kredity = 0
povinne = 0
pv1 = 0
pv2 = 0
volitelne = 0
hotovo = []
while kredity < 180 or pv1 < 6 or pv2 < 15:
	
	print()
	predmet = input("Zadej kredity a typ, například: 15 v: ")
	kredit, typ = predmet.split(" ")
	
	if typ == "pv1":
		pv1 += int(kredit)
		if pv1 >= 6  and "pv1" not in hotovo:
			hotovo.append("pv1")
	elif typ == "pv2":
		pv2 += int(kredit)
		if pv2 >= 15 and "pv2" not in hotovo:
			hotovo.append("pv2")
	elif typ == "v":
		volitelne += int(kredit)
	elif typ == "p":
		povinne += int(kredit)

	if volitelne > 27:
			volitelne = 27

	kredity = pv1 + pv2 + povinne + volitelne
	
	print(f"Máš {kredity}/180 kreditů celkově, {pv1}/6 za pv1, {pv2}/15 za pv2 a {volitelne}/27 za v")
	if len(hotovo) == 0:
		print("Nemáš nic splněno :-(")
	else:
		print("Máš splněno: ", end = "")
		for i in hotovo:
			print(i, end = " ")
else:
	print("-> Lolz zvládls to")
