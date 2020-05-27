import scipy.io
import numpy
#import k-means 

def main():
    data = scipy.io.loadmat('./data/exapmle.mat')  # 读取mat文件
    i = 0
    for row in data:
        if i>2:
            print("**"+data[row][0]['Alpha'][0][0]+"**: "+data[row][0]['Description'][0][0])
        i=i+1
    print(i)
            
    # print(data['ESN_2']['data'])
    # print(data['ESN_2']['Rate'])
    # print(data['ESN_2']['Units'])
    # print(data['ESN_2']['Description'])
    # print(data['ESN_2']['Alpha'])
    # for col in data['ESN_2']:
    #     print(col)
    # while i<100:
    #     i=i+1
    #     print(data[i])
    # print(data)

    

if __name__=="__main__":
    main()
