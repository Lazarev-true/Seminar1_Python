# Напишите программу для проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

for X in range(2):
    for Y in range(2):
        for Z in range(2):
            first = not(X or Y or Z)
            second = not X and not Y and not Z

            if first == second:
                print(f'{X} {Y} {Z} -> Истинно')
            else:
                print(f'{X} {Y} {Z} -> Неистинно')