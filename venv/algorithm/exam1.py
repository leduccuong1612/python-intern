def sum():
    ops = ["+","-",""]
    listt = []
    for a in range(len(ops)):
        for b in range(len(ops)):
            for c in range(len(ops)):
                for d in range(len(ops)):
                    for e in range(len(ops)):
                        for f in range(len(ops)):
                            for g in range(len(ops)):
                                for h in range(len(ops)):
                                    for i in range(len(ops)):
                                        if(ops[a] != "+"):
                                            tuplee = (ops[a],ops[b],ops[c],ops[d],ops[e],ops[f],ops[g],ops[h],ops[i])
                                            listt.append(tuplee)
    for f in listt:
        if( eval("{}1{}2{}3{}4{}5{}6{}7{}8{}9".format(*f)) == 100):
         print(("{}1{}2{}3{}4{}5{}6{}7{}8{}9".format(*f)))
sum()