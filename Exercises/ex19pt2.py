def number_of_pens(pens_per_pack, number_of_packs):
	print("There are %r pens in a pack" % pens_per_pack)
	print("There are %r packs of pens" % number_of_packs)
	total_pens = pens_per_pack * number_of_packs
	print("You have %r pens" % total_pens)

number_of_pens(int(input("how many pens?")), int(input("how many packs?")))