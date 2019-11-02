from sklearn import svm  
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
import time
# 读取数据
data = pd.read_csv('image_data_correct.csv') 
data=np.array(data)
rate=[]
Kernel='rbf'
epoch=100
maxrate=0
meanrate=0
meantime=0
for k in range(epoch):
    # 划分训练集测试集
    X_train,X_test, y_train, y_test  = train_test_split(data[:, 1:11], data[:, 11], test_size=0.2, random_state=k)   
    # 搭建svm模型
    svm_clf=svm.SVC(C=1, kernel=Kernel, degree=3, gamma='auto', coef0=0.0, shrinking=True, \
                    probability=False,tol=0.001, cache_size=400, class_weight=None, verbose=False, \
                    max_iter=-1, decision_function_shape=None,random_state=None)
    # 训练模型
    print('Training begin...')
    start=time.clock()
    svm_clf.fit(X_train, y_train) 
    end=time.clock()
    print('Training finish')
    print('Train Time: ',end-start)
    meantime=meantime+(end-start)
    # 测试模型
    y_pre = svm_clf.predict(X_test)
    print('y_predict', y_pre)
    print('y_true', y_test)
    # 计算准确率
    #（0机械损伤，1霉变，2虫蛀）
    sum=0
    for i in range(len(y_test)):
        if y_pre[i]==y_test[i]:
            sum=sum+1
        else:
            print('the predict is ',y_pre[i],', but the true is ',y_test[i])
    print('测试集大小', len(y_test))
    print('预测正确个数', sum)
    print('epoch[', k+1, '] ', sum/len(y_test))
    rate.append(sum/len(y_test))
    print('')
    meanrate+=rate[k]
    if rate[k]>maxrate:
        maxrate=rate[k];
print('所用核为：',Kernel)
print('最高准确率：', maxrate)
print('平均准确率：', meanrate/epoch)
print('平均训练用时：', meantime/epoch)


