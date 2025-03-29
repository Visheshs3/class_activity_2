def find_cube_pairs(target):  #  --> adding :
    solutions = []   # ; --> nothing
    max_num = round(target ** (1/3))  # targ --> target, *** -> **  

    for a in range(1, max_num + 1):   # ranges --> range
        for b in range(a, max_num + 1):   # adding :
            if a**3 + b**3 == target:   # adding : and *** -> **   
                solutions.append((a, b))  # sol --> solutions
    return solutions

pairs = find_cube_pairs(1729) # , to  null
print("Valid cube pairs for 1729:")  # printf to print 1728 -> 1729
for i in pairs:     # pair- > pairs: only 1 required 
    a,b =i  #unpacking tuple
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729") # printf to print and 1728 -> 1729  a^2 and b^2 to a^3 and b^3