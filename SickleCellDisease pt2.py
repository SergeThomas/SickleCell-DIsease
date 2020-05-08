#Function to return DNA slc sequences.
def translate(seq):
    table = {
            'ATT':'I', 'ATC':'I', 'ATA':'I',
            'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L', 'TTA':'L','TTG':'L',
            'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
            'TTT':'F', 'TTC':'F',
            'ATG':'M'
            }
    DNA = ""
    if len(seq):
        if len(seq)%3 != 0:
                seq = seq[0:-1]
                if len(seq)%3 != 0:
                    seq = seq[0:-1]
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            try:
                DNA += table[codon]
            except:
                DNA += "X"
    return DNA

#Function identifies the lowercase a in the DNA file and converts it to A and T then prints it out to respective text files
def mutate():
    DNA = open("DNA.txt","r")
    normDna = open('normalDNA.txt','w')

    normalDNA = DNA.read().replace('a','A')
    normalDnaCopy = normDna.write(normalDNA)

    print(normalDNA)

    DNA.close()
    normDna.close()

    DNA = open("DNA.txt", "r")
    muteDna = open('mutatedDNA.txt','w')

    mutateDNA = DNA.read().replace('a','T')
    mutateDnaCopy = muteDna.write(mutateDNA)

    print(mutateDNA)

    DNA.close
    muteDna.close()
# mutate() to test the function

#This function is the transalate function.
def txtTranslate(inputFile):
    #We call the readVariable as the read function so it can first read the file and then call it within the transalate function that way it converts the file and stores it in the readVar.
    readVar = translate(read_seq(inputFile))
    print(readVar)
    return readVar

#This function opens up a file and reads its inputs
def read_seq(inputFile):
    with open(inputFile, "r") as f:
        seq = f.read()
    seq = seq.replace("\n", "")
    return seq

#This will print out all the results and return the converted versions.
txtTranslate("normalDNA.txt")
txtTranslate("mutatedDNA.txt")