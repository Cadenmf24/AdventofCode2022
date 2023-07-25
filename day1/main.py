import elves
        
def day1():

    gary = elves.Elf('Gary', [1000, 2000, 3000])
    larry = elves.Elf('Larry', [4000])
    barry = elves.Elf('Barry', [5000, 6000])
    carry = elves.Elf('Carry', [7000, 8000, 9000])
    bob = elves.Elf('Bob', [10000])



    party = [gary, larry, barry, carry, bob]

    for i in party:
        print(i.getName(), i.getTotal())


    
    print(gary.compare(party))

day1()