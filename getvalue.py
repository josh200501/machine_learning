# -*- coding: utf8 -*-
import preprocess
import preprocesssample
import getlog
from numpy import *
import matplotlib.pyplot as plt

def loaddataset():
    md5 = getlog.getmd5()
    vector_all = preprocess.final()
    res = [0]*len(vector_all)
    dataMat = []
    datalength = []
    for i in md5:
        vector_sample = preprocesssample.final(i)
        length = float(len(vector_sample))
        for i in vector_sample:
            if i in vector_all:
                res[vector_all.index(i)] = 1
        res2 = map(float, res)
        res2 = res2/(distEclud(mat(res2),0))
        #print 'res', res
        #print 'res2', res2
        dataMat.append(res2)      
        for i in range(len(res)):
            res[i] = 0
        #print 'length', length
        datalength.append(length)
    
    print datalength
    #print dataMat
    print 'shape of dataMat: ', shape(dataMat)
    return dataMat, datalength

def distEclud(vecA,vecB):
    return sqrt(sum(power(vecA-vecB, 2)))

def randCent(dataset, k):
    n = shape(dataset)[1]
    centroids = mat(zeros((k, n)))
    for j in range(n):
        minJ = min(dataset[:,j])
        rangeJ = float(max(dataset[:,j]) - minJ)
        centroids[:,j] = minJ + rangeJ * random.rand(k,1)
    return centroids

def kMeans(dataset, k, distMeas=distEclud, createCent=randCent):
    m = shape(dataset)[0]
    clusterAssment = mat(zeros((m,2)))
    centroids = createCent(dataset, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf; minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataset[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
        #print centroids
        for cent in range(k):
            ptsInClust = dataset[nonzero(clusterAssment[:,0] .A==cent)[0]]
            centroids[cent,:] = mean(ptsInClust, axis=0)
    return centroids, clusterAssment

def biKmeans(dataset, k, distMeas=distEclud):
    m = shape(dataset)[0]
    clusterAssment = mat(zeros((m,2)))
    centroid0 = mean(dataset, axis=0).tolist()[0]
    centList = [centroid0]
    for j in range(m):
        clusterAssment[j,1] = distMeas(mat(centroid0), dataset[j,:])**2
    while (len(centList) < k):
        lowestSSE = inf
        for i in range(len(centList)):
            ptsInCurrCluster = \
            dataset[nonzero(clusterAssment[:,0].A==i)[0],:]
            centroidMat, splitClustAss = \
            kMeans(ptsInCurrCluster, 2, distMeas)
            sseSplit = sum(splitClustAss[:,1])
            sseNotSplit = \
            sum(clusterAssment[nonzero(clusterAssment[:,0].A!=i)[0],1])
            print "sseSplit, and notSplit: ",sseSplit, sseNotSplit
            if(sseSplit + sseNotSplit) < lowestSSE:
                bestCentToSplit = i
                bestNewCents = centroidMat
                bestClustAss = splitClustAss.copy()
                lowestSSE = sseSplit + sseNotSplit
        bestClustAss[nonzero(bestClustAss[:,0].A == 1)[0],0] = \
        len(centList)
        bestClustAss[nonzero(bestClustAss[:,0].A == 0)[0],0] = \
        bestCentToSplit
        print 'the bestCentToSplit is: ',bestCentToSplit
        print 'the len of bestClustAss is: ',len(bestClustAss)
        centList[bestCentToSplit] = bestNewCents[0,:]
        centList.append(bestNewCents[1,:])
        clusterAssment[nonzero(clusterAssment[:,0].A == \
                               bestCentToSplit)[0],:] = bestClustAss
        print 'shape of centList',shape(centList)
    return centList, clusterAssment
    
if __name__ == '__main__':
    print 'hello'
    datamat, lengthlist = loaddataset()
    datamat = mat(datamat)
    #mycentorids, clustassing = kMeans(datamat, 2)
    centlist, clustassing = biKmeans(datamat,2)
    '''
    print'mycentorids:'
    print mycentorids
    '''
    print 'clustassing:'
    #print clustassing
    print clustassing
    
    length = shape(datamat)[0]
    length1 = shape(datamat)[1]
    x = [0.0]*length
    y = [0.0]*length
    z = [0.0]*length1
    for i in range(length):
        x[i]=i
        #y[i]=distEclud(datamat[i,:], z)
        y[i]=lengthlist[i]
    scale = array(clustassing[:,0])
    scale = scale + 1
    print 'scale',scale
    plt.scatter(x, y, 25.0*scale, 25.0*scale, alpha=0.9)
    plt.show()  
    