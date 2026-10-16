import numpy as np

def load_data(filename):
    age=[]
    hg=[]
    cls=[]
    with open(filename,"r") as file:
        header = file.readline() #seperate header
        for line in file:
            formatted=line.strip().split() #seperate each line into its parts
            age.append(int(formatted[0]))
            hg.append(int(formatted[1]))
            cls.append(int(formatted[2]))
    return age, hg, cls



def perceptron(age, hg, cls):
    np.random.seed(26)
    w0=np.random.uniform(-1,1)
    w_age=np.random.uniform(-1,1)
    w_hg=np.random.uniform(-1,1)
    y=[] #convert the 1s and 0s to 1s and -1
    for i in range(len(cls)):
        if cls[i]==0:
            y.append(-1)
        else:
            y.append(1)


    for step in range(10000000):
        mistakes=0 #counter to see when all points have been sorted correctly
        for i in range(len(age)):
            output = w0 + w_age*age[i] + w_hg*hg[i]
            if y[i]*output <=0: #test to see if the point is on the correct side
                w0 = w0 + y[i] #if prediction is wrong move the line
                w_age = w_age + y[i] * age[i]
                w_hg = w_hg + y[i] * hg[i]
                mistakes=mistakes+1
        if mistakes==0: #if loop runs with no mistakes then end
            break
    return w0, w_age, w_hg

age, hg, cls=load_data("stroke_separable.csv")
w0, w_age, w_hg=perceptron(age, hg, cls)
#print(w0, w_age, w_hg)




    

    



        
  

        


