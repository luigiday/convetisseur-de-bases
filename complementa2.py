def complementa2(n):
    nb = bin(n)
    if n >= 0:
        nb = nb[2:]
        if len(nb) < 8:
            nblist = []
            for i in range(8-len(nb)):
                nblist.append(0)
        elif len(nb) < 16:
            nblist = []
            for i in range(16-len(nb)):
                nblist.append(0)
        elif len(nb) < 32:
            nblist = []
            for i in range(32-len(nb)):
                nblist.append(0)
        elif len(nb) < 64:
            nblist = []
            for i in range(64-len(nb)):
                nblist.append(0)
        for x in nb:
            nblist.append(int(x))
        detail = "Conversion normale en binaire"
        return(nblist, detail)
    else:
        nb = nb[3:]
        detail = "Nombre negatif :"
        if len(nb) < 8:
            nblist = []
            for i in range(8-len(nb)):
                nblist.append(0)
            for x in nb:
                nblist.append(int(x))
            detail += f"\nConversion en binaire sur 8 bits : {nblist}"
            for i, e in enumerate(nblist):
                nblist[i] = 1 - e
            detail += f"\nInversion des bits : {nblist}"
            carry = 1
            for i in range(7, -1, -1):
                if nblist[i] == 1 and carry == 1:
                    nblist[i] = 0
                elif nblist[i] == 0 and carry == 1:
                    nblist[i] = 1
                    carry = 0
            detail += f"\nAjout de 1 : {nblist}\n"
        elif len(nb) < 16:
            nblist = []
            for i in range(16-len(nb)):
                nblist.append(0)
            for x in nb:
                nblist.append(int(x))
            detail += f"\nConversion en binaire sur 16 bits : {nblist}"
            for i, e in enumerate(nblist):
                nblist[i] = 1 - e
            detail += f"\nInversion des bits : {nblist}"
            carry = 1
            for i in range(15, -1, -1):
                if nblist[i] == 1 and carry == 1:
                    nblist[i] = 0
                elif nblist[i] == 0 and carry == 1:
                    nblist[i] = 1
                    carry = 0
            detail += f"\nAjout de 1 : {nblist}\n"
        elif len(nb) < 32:
            nblist = []
            for i in range(32-len(nb)):
                nblist.append(0)
            for x in nb:
                nblist.append(int(x))
            detail += f"\nConversion en binaire sur 32 bits : {nblist}"
            for i, e in enumerate(nblist):
                nblist[i] = 1 - e
            detail += f"\nInversion des bits : {nblist}"
            carry = 1
            for i in range(31, -1, -1):
                if nblist[i] == 1 and carry == 1:
                    nblist[i] = 0
                elif nblist[i] == 0 and carry == 1:
                    nblist[i] = 1
                    carry = 0
            detail += f"\nAjout de 1 : {nblist}\n"
        elif len(nb) < 64:
            nblist = []
            for i in range(64-len(nb)):
                nblist.append(0)
            for x in nb:
                nblist.append(int(x))
            detail += f"\nConversion en binaire sur 64 bits : {nblist}"
            for i, e in enumerate(nblist):
                nblist[i] = 1 - e
            detail += f"\nInversion des bits : {nblist}"
            carry = 1
            for i in range(63, -1, -1):
                if nblist[i] == 1 and carry == 1:
                    nblist[i] = 0
                elif nblist[i] == 0 and carry == 1:
                    nblist[i] = 1
                    carry = 0
            detail += f"\nAjout de 1 : {nblist}\n"
        else:
            raise ValueError("Le nombre est trop grand pour être représenté en complément à 2 sur 64 bits")
        return(nblist, detail)

