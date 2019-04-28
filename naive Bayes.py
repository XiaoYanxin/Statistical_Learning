import numpy as np

def naive_bayes_classifier(feature,label,input_data):
    label_category  = list((set(label)))
    label_number = len(label_category)
    label_pro = {}
    for i in range(label_number):
        label_pro[label_category[i]] = (len(label[label == label_category[i]])+1) / (len(label)+len(label_category))
    print('label_pro:',label_pro)

    len_feature = len(feature)
    feature_set = {}
    for i in range(len_feature):
        feature_set[i] = list(set(feature[i]))

    feature_label_pro = {}
    for k in range(label_number):
        label_select = label[label==label_category[k]]
        denominator = len(label_select)
        label_index = np.where(label == label_category[k])
        for i in range(len_feature):
            for j in range(len(feature_set[i])):
                object_feature = np.array(feature[i])[label_index]
                numerator = len(object_feature[object_feature==feature_set[i][j]])
                feature_label_pro_key = str(i)+str(feature_set[i][j])+str(label_category[k])
                feature_label_pro[feature_label_pro_key] = (numerator+1) / (denominator+len(feature_set[i]))
    print('feature_label_pro:',feature_label_pro)
    calc_label_prob = {}
    for i in label_category:
        mul=label_pro[i]
        for j in range(len(input_data)):
            mul*=feature_label_pro[str(j)+str(input_data[j])+str(i)]
        calc_label_prob[str(i)]=mul
    print(calc_label_prob)
    return max(calc_label_prob,key = calc_label_prob.get)

if __name__ == '__main__':
    features = [[1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],
                ['S', 'M', 'M', 'S', 'S', 'S', 'M', 'M', 'L', 'L', 'L', 'M', 'M', 'L', 'L']]
    features = np.array(features)
    label = [-1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1]
    label = np.array(label)
    input_data = np.array([2, 'S'])
    output_label = naive_bayes_classifier(features, label, input_data)
    print("the output label of input_data is:{}".format(output_label))
