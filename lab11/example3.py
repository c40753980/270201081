class DNA:
    
    def __init__(self,dna):
        self.dna = dna
       
    def count_nuclentides(self):
        count = {"A":0,"G":0,"C":0,"T":0}
        for x in self.dna:
            count [x] += 1
        return count
    
    def calculate_complement(self):
        new_dna = ""
        reversed_dna = self.dna[::-1]
        for x in reversed_dna:
            if x=="A":
                new_dna += "T"
            elif x=="T":
                new_dna += "C"
            elif x=="C":
                new_dna += "G"
            elif x=="G":
                new_dna += "C" 
                
        return DNA(new_dna)       

    def count_point_mutations(self,dna):
        count = 0
        
        for i in range(len(self.dna)):
            if self.dna[i] == dna.dna[i]:
                count += 1
        return count  
    
    def find_motif(self,dna1):
         location = []
         for i in range(len(self.dna) - len(dna.dna)+1):
             if self.dna[i:i+dna1.dna] == dna1.dna :
                 location.append(i)
         return location     




       
dna = DNA("ATCCGATAA")
print(dna.calculate_complement().dna) 
       