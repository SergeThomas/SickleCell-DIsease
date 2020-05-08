#Function to return DNA slc sequences.
def translate(seq):
    table = {
            'ATT':'I', 'ATC':'I', 'ATA':'I',
            'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L', 'TTA':'L','TTG':'L',
            'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
            'TTT':'F', 'TTC':'F',
            'ATG':'M'
            }
    DNA = ""    #DNA is an empty string because we will add unto it later in the program

    #The if statement basically reads through the table get the length of the string. If it is divisible by three and not zero it will match it to a codon up in the table and return its letter. 
    if len(seq):
        if len(seq)%3 != 0:
            seq = seq[0:-1]
            if len(seq)%3 != 0:
                seq = seq[0:-1]
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            DNA += table[codon]
            try:    #This is basically here so that if the user enters a codon that isnt in the table it will return X
                DNA += table[codon]
            except:
                DNA += "X"
    return DNA

#Gets user input to put out codon
userInput = input("Enter DNA sequence (e.g ATTATTATT):   ")

#This prints the translated user input
print(translate(userInput))

