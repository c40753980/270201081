class DNA:
    def __init__(self, dna):
        self.dna = dna

    def count_nucleotids(self):
        dna_dictionary = dict()
        counter_A = 0
        counter_C = 0
        counter_G = 0
        counter_T = 0
        for i in self.dna:
            if i == "A":
                counter_A += 1
                dna_dictionary[i] = counter_A
            elif i == "C":
                counter_C += 1
                dna_dictionary[i] = counter_C
            elif i == "G":
                counter_G += 1
                dna_dictionary[i] = counter_G
            else:
                counter_T += 1
                dna_dictionary[i] = counter_T

        return dna_dictionary

    def calculate_complement(self):
        antidna = ""
        for i in self.dna:
            if i == "A":
                antidna = antidna + "T"
            elif i == "C":
                antidna = antidna + "G"
            elif i == "G":
                antidna = antidna + "C"
            else:
                antidna = antidna + "A"
        return antidna

    def count_point_mutations(self, mutateddna):
        if len(mutateddna) == len(self.dna):
            counter = 0
            mutation = 0
            while counter < len(mutateddna):
                if self.calculate_complement()[counter] != mutateddna[counter]:
                    mutation = mutation + 1
                counter = counter + 1
            return mutation

    def find_motif(self, subdna):
        listof = list()
        counter = len(self.dna)
        temp = len(subdna)
        index = 0
        while counter != 0:
            if self.dna[index:temp] == subdna:
                listof.append(index)
            index = index + 1
            temp = temp + 1
            counter = counter - 1
        return listof


mydna = DNA("GATATATGCATATACTT")
print(mydna.count_nucleotids())
print(mydna.calculate_complement())
print(mydna.count_point_mutations("CGTATAACGTTATACTT"))
print(mydna.find_motif("ATAT"))