def hamster_me(code, message):
    sortCode = sorted(list(set(code)))
    Start = sortCode[0]
    ans = []
    result = []
    # Array
    while True:
        List = []
        try: 
            for character in map(chr, range(ord(sortCode[0]),ord(sortCode[1]))):
               List.append(character)
            ans.append(List)     
            sortCode.pop(0)
        except:
            for character in map(chr, range(ord(sortCode[0]),123)):
               List.append(character)
            for character in map(chr, range(97,ord(Start))):
               List.append(character)
            ans.append(List)
            break  
    # Coding
    for letter in message:
        for column in ans:
            if column[0] == letter:
                Tuple = (letter,'1')
                result.append(Tuple)
            else:
                for item in column:
                    if item == letter:
                        Tuple = (column[0],str(column.index(item)+1))
                        result.append(Tuple)
    Ans =  ''.join([i for sub in result for i in sub]) 
    return Ans

hamster_me("hhhhammmstteree", "hamster")