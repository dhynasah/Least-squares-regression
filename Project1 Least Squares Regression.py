import matplotlib.pyplot as plt
import numpy as np
import csv

def sumX(x):
    sumX=np.sum(x) 
    return sumX

#returns the sum of all Y values
def sumY(y):
    sumY=np.sum(y)
    return sumY

#returns the sum of the products of each X,Y pair
def product_pair(x,y):
   prodPairSum=0
   x_len = len(x)
   for i in range(0,x_len):
       xval = x[i]
       yval= y[i]
       prodPairSum = xval*yval + prodPairSum
       
   return prodPairSum

#returns the sum of the squares of every X value
def SquaresX_Sum(x):
    xsq=[]
    for i in x:
       x2= i*i
       xsq.append(x2)
    sumSqX = np.sum(xsq)
    return sumSqX

#returns the sume of the squares of every Y value 
def SquaresY_Sum(y):
    ysq=[]
    for i in y:
        y2 = i*i
        ysq.append(y2)
        sumSqY=np.sum(ysq)
        return sumSqY
 # returns the slope 
def slope(x,y):
   sumSqY= SquaresY_Sum(x)
   sumSqX = SquaresX_Sum(y)
   prodPair = product_pair(x,y)
   sumYs = sumY(y)
   sumXs = sumX(x)
   m = (prodPair-(sumXs*sumYs))/(sumSqX-sumSqY) #slope  
   return m

# returns the intercept 
def intercept(x,y,N):
    m = slope(x,y)
    sumYs= sumY(y)
    sumXs= sumX(x)
    b = (sumYs-(m*sumXs))/N #intercept 
    return b

def main():
    with open('downloads.txt') as oldFile, open('Books.txt','w') as newFile:
        for line in oldFile:
            if "nan" not in line:
                newFile.write(line)
    oldFile.close()
    newFile.close()

    x =[]
   
    y= []
    N = len(x)
    print (N)
    with open("Books.txt","r") as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(int(row[0]))
            y.append(int(row[1]))


        
    plt.scatter(x,y)
    plt.xlabel('hour')
    plt.ylabel('Books')
    plt.title('Books Downloaded per hour')
    
    plt.show()
   
    
    N = len(x)
    R = len(y)
    print(R)
    print(N)
    sumx= sumX(x)
    print(sumx)

    sumy = sumY(y)
    print(sumy)

    prodpair = product_pair(x,y)
    print (prodpair)

    sumSqx= SquaresX_Sum(x)
    print(sumSqx)

    sumSqy = SquaresY_Sum(y)
    print(sumSqy)

    slop = slope(x,y)
    print(slop)

    b = intercept(x,y,N)
    print(b)
    
    # 5th day at noon regression equation
    ys = slop*108+b
    print(ys, "number of books on 5th day")
    # generate linear fit
    fit = np.polyfit(x,y,1)
    fit_fn= np.poly1d(fit)
    
    plt.plot(x,y, 'o', x, fit_fn(x))
    plt.xlim(0,800)
    plt.ylim(0,6500)
     
    
   
if __name__ == "__main__":
    main()