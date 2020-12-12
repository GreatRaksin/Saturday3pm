print('\tОснова\tМясо\tСоус\tПомидорки\tСалат')
count = 1
var = [0, 1]
for base in var:
    for meat in var:
        for sauce in var:
            for pomidorki in var:
                for salad in var:
                    print(f'№{count} \t', end='')
                    print(f'{base}\t{meat}\t{sauce}\t{pomidorki}\t{salad}', end='')
                    print()
                    count += 1