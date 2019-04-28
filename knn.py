import numpy as np
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('mnist_data/',one_hot=True)
print('data is ok')
Xtrain,Ytrain = mnist.train.next_batch(5000)
Xtest ,Ytest = mnist.test.next_batch(200)
print('Xtrain.shape:',Xtrain.shape,'Xtest.shape:',Xtest.shape)
print('Ytrain.shape:',Ytrain.shape,'Ytest.shape:',Ytest.shape)

xtrain = tf.placeholder('float',[None,784])
xtest = tf.placeholder('float',[784])

distance = tf.reduce_sum(tf.abs(tf.add(xtrain,tf.negative(xtest))),axis=1)
pre = tf.argmin(distance,0)

init = tf.global_variables_initializer()
accuracy = 0

with tf.Session() as sess:
    sess.run(init)
    Ntest = len(Xtest)
    for i in range(Ntest):
        nn_index = sess.run(pre,feed_dict={xtrain:Xtrain,xtest:Xtest[i,:]})
        pred_class_label = np.argmax(Ytrain[nn_index])
        true_class_label = np.argmax(Ytest[i])
        if pred_class_label==true_class_label:
            accuracy+=1
    print('ACC:',accuracy/Ntest)
