class Pair:
    # initialize used variables and Lists
    FilePath  = Prefix = Suffix = Sequence = ""
    distance = Kmers = 0
    partone = []
    parttwo = []
    start = None
    End = None
    Seq = {}
    def __init__(self, path): # Constructor to Get File Path and Distance Entered by user
        self.FilePath = path

    def OpenFile(self): # Function to read txt file split each part in partone list and the other in parttwo list
        with open(self.FilePath) as file:
            for i, line in enumerate(file):
                if i == 0:
                    line = line.rstrip().split(' ')
                    self.Kmers = int(line[0])
                    self.distance = int(line[1])
                else:
                    line = line.rstrip().split('|')
                    self.partone.append(line[0])
                    self.parttwo.append(line[1])
        
    def Graph(self): # Function for Creating the Graph {(prefix1,prefix2):(suffix1,suffix2)}
        for i in range(len(self.partone)): 
                self.Seq[(self.partone[i][:self.Kmers - 1],self.parttwo[i][:self.Kmers - 1])] = (self.partone[i][1:],self.parttwo[i][1:])



    def StartEndPos(self): # Function to get Start of our path and its end 
        temp = self.Seq.copy()
        for key,val in self.Seq.items():
            for valu in self.Seq.values():
                if key == valu:
                    del temp[key]
        self.start = temp
        temp1 = self.Seq.copy()
        for key,val in self.Seq.items():
            for k,valu in self.Seq.items():
                if val == k:
                    del temp1[key]
        self.End = temp1

    def assemble(self): # starting with our start till the end adding first letter in everyone except last one add all its letters
        myend = list(self.End.values()) # our End
        y = list(self.start.keys())
        start = y[0] # Our Start
        self.Prefix = start[0][0] # add first letter for start in Prefix
        self.Suffix = start[1][0] # add first letter for start in Suffix
        next = self.Seq[start] # Get next one
        while True:
            if next == myend[0]: # if next one equals last 
                self.Prefix += next[0] # add all letters to Prefix
                self.Suffix += next[1] # add all letters to Suffix
                break
            else: # next one not last 
                self.Prefix += next[0][0] # add first letter of next to Prefix
                self.Suffix += next[1][0] # add first letter of next to Suffix
                next = self.Seq[next] # Get next one
                

    def GetSequence(self):# Function to Generate Sequence
        # by adding prefix and last (Kmers+Distance) letters from suffix end
        self.Sequence += self.Prefix # add Prefix to Genome
        LOS = self.distance + self.Kmers # cal number of letters to be taken from Suffix
        self.Sequence += self.Suffix[-LOS:] # Get last (Kmers+Distance) letters from suffix end 

    def predict(self): # Function To call other functions used to predict the Sequence and return it
        # to be displayed in the GUI
        self.OpenFile()
        self.Graph()
        self.StartEndPos()
        self.assemble()
        self.GetSequence()
        return self.Sequence

if __name__ == "__main__":
    file = input("Enter file path: ")
    p = Pair(file)
    output = p.predict()
    print("Your output is: ")
    print(output)
