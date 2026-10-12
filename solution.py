def load_data(filename):
    age=[]
    hg=[]
    cls=[]
    with open(filename,"r") as file:
        header = file.readline() #seperate header
        for line in file:
            formatted=line.strip().split() #seperate each line into its parts
            age.append(formatted[0])
            hg.append(line[1])
            cls.append(line[2])
    return age, hg, cls

load_data("stroke_seperable.csv")  

def perceptron(age, hg, cls):
    



        
  

        


