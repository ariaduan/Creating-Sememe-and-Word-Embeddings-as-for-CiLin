import numpy as np
from math import sqrt

def cos_sim(vector_a, vector_b):
    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim
'''
Author：衣介书生
Link：https://www.jianshu.com/p/0c33c17770a0
'''

def multi_vec(vector_a,x):
    vector_a = np.mat(vector_a)
    return vector_a*x


file1 = open('../models/cb_cilin_def_palin_3.vector','rb')#replace this file with the one you want to use
file2 = open('../files/WS_sememes_1','rb')
file3 = open('../files/WS_sememes_2','rb')
fileout = open('../results/WS_resem_baseline_simi_cb_cilin_def_palin_3','w',encoding = 'utf-8')#replace this file in correspondence with the name of file1

line1 = file1.readline()

bank = []
vec = []
for line1 in file1:
    line1 = line1.decode('utf-8')
    tmp1 = line1.split()
    bank.append(tmp1[0])
    vec.append(list(map(float,tmp1[1:])))

y = []
score = []
for line2 in file2:
    line2 = line2.decode('utf-8')
    tmp2 = line2.split()
    line3 = file3.readline().decode('utf-8')
    tmp3 = line3.split()
    if tmp2[0] == '&':
        m = max(score)
        fileout.write(str(m) + ',')
        y.append(m)
        score = []
        continue
    length1 = len(tmp2)
    length2 = len(tmp3)
    semvec1 = np.mat(0)
    semvec2 = np.mat(0)
    for i in range(len(tmp2)-1,-1,-1):
        ix = bank.index(tmp2[i])
        tmp = multi_vec(vec[ix],1/(2**(len(tmp2)-i))) if (i != 0) else multi_vec(vec[ix],1/(2**(len(tmp2)-i-1)))
        semvec1 = semvec1 + np.mat(tmp)
    for i in range(len(tmp3)-1,-1,-1):
        ix = bank.index(tmp3[i])
        tmp = multi_vec(vec[ix],1/(2**(len(tmp3)-i))) if (i != 0) else multi_vec(vec[ix],1/(2**(len(tmp3)-i-1)))
        semvec2 = semvec2 + np.mat(tmp)

    total = cos_sim(semvec1,semvec2)
    score.append(total)

 
def multipl(a,b):
    sumofab=0.0
    for i in range(len(a)):
        temp=a[i]*b[i]
        sumofab+=temp
    return sumofab
 
def corrcoef(x,y):
    n=len(x)
    #求和
    sum1=sum(x)
    sum2=sum(y)
    #求乘积之和
    sumofxy=multipl(x,y)
    #print(sumofxy)
    #求平方和
    sumofx2 = sum([pow(i,2) for i in x])
    sumofy2 = sum([pow(j,2) for j in y])
    num=sumofxy-(float(sum1)*float(sum2)/n)
    #print(sum1,sum2,sumofx2,sumofy2,(sum1**2)/n,(sum2**2)/n)
    #计算皮尔逊相关系数
    #print((sumofx2-float(sum1**2)/n)*(sumofy2-float(sum2**2)/n))
    den=sqrt((sumofx2-float(sum1**2)/n)*(sumofy2-float(sum2**2)/n))
    return num/den
 
x = [0.9960000000000001,0.9777777777800001,0.94444444444,0.9192592592600001,0.916,0.8583999999999999,0.8562962963,0.8488888888,0.84814814814,0.8207407408,0.8081481481400001,0.79777777778,0.7936,0.7822222222199999,0.77037037038,0.7637037037,0.7584,0.7552,0.7535999999999999,0.75037037038,0.7496,0.7474074074,0.7376,0.72888888888,0.728,0.71851851852,0.7177777777800001,0.716,0.7088,0.7066666666,0.7064,0.705925926,0.696,0.6925925926,0.6872,0.6832,0.6799999999999999,0.6755555556,0.6711111112,0.6704,0.6703703703799999,0.6696,0.65407407408,0.65384615384,0.6519999999999999,0.65076923076,0.64222222222,0.6407407408,0.6392592592599999,0.63851851852,0.636,0.6333333334,0.632,0.63037037038,0.62962962962,0.6288,0.62666666666,0.624,0.624,0.6192592591999999,0.6155555555600001,0.6152,0.61384615384,0.6128,0.6048,0.60074074074,0.6,0.6,0.5962962962,0.596,0.5955555556000001,0.5955555555600001,0.5936,0.5903703704,0.58962962962,0.5896,0.5856,0.5831999999999999,0.58222222222,0.5816,0.5784,0.57777777778,0.57703703704,0.5711999999999999,0.5704,0.5648,0.564,0.5562962963,0.5533333334,0.5456000000000001,0.54518518518,0.5448000000000001,0.5424,0.54222222222,0.54148148148,0.54148148148,0.54,0.5344,0.5333333334,0.5325925926,0.532,0.5296000000000001,0.5296000000000001,0.5288888888,0.52666666666,0.5232,0.5232,0.5214814814000001,0.52,0.51851851852,0.5168,0.51185185186,0.5111111112,0.5066666665999999,0.5048,0.5037037037000001,0.5032,0.5,0.49925925926000003,0.49925925926000003,0.4962962963,0.49481481479999995,0.4944,0.4944,0.4933333334,0.4933333334,0.4874074074,0.4874074074,0.48719999999999997,0.4856,0.4856,0.48319999999999996,0.4824,0.4824,0.4728,0.46592592592,0.4648,0.4637037038,0.46296296296,0.45919999999999994,0.45759999999999995,0.4528,0.45119999999999993,0.45037037038000005,0.44962962961999997,0.44800000000000006,0.4385185186,0.4362962963,0.43520000000000003,0.43360000000000004,0.43200000000000005,0.4312,0.43111111112,0.43037037038000003,0.42962962962000006,0.42560000000000003,0.4248,0.4248,0.4248,0.42000000000000004,0.4162962963,0.4162962963,0.4112,0.4111111112,0.4104,0.4088,0.4072,0.40592592592,0.40370370380000004,0.4032,0.40296296295999995,0.4016,0.4008,0.4,0.4,0.3992592592,0.39037037038,0.3837037038,0.3807407408,0.38074074073999997,0.38,0.3785185186,0.3748148148,0.3728,0.37037037038,0.36960000000000004,0.368,0.36560000000000004,0.36074074079999996,0.36,0.36,0.3592,0.35851851852,0.35333333334,0.352,0.3474074074,0.3464,0.34370370370000003,0.3432,0.33999999999999997,0.3376,0.3312,0.32296296296000004,0.3162962962,0.3125925926,0.3103703704,0.3048,0.3037037037,0.30148148148,0.30148148140000003,0.29407407407999997,0.28959999999999997,0.2888,0.2888,0.28808,0.2832,0.28222222222000004,0.28222222220000004,0.28148148148,0.27555555556,0.27414814814,0.27185185186,0.2712,0.27037037038,0.26444444444,0.264,0.25680000000000003,0.2552,0.2548148148,0.2488,0.24559999999999998,0.24444444440000002,0.244,0.2437037038,0.23925925925999997,0.23925925925999997,0.2384,0.23703703703999998,0.23481481482,0.23037037040000002,0.22888888887999997,0.225925926,0.21760000000000002,0.21481481482000003,0.20962962959999998,0.20814814814,0.20666666660000002,0.20518518518,0.1985185186,0.1977777778,0.1874074074,0.18518518518,0.18444444444000002,0.184,0.18148148148,0.1752,0.1712,0.165925926,0.1592,0.15777777778,0.1552,0.15360000000000001,0.14296296296,0.13185185185999998,0.12666666665999998,0.12370370369999999,0.12222222220000001,0.1216,0.11439999999999999,0.09925925926,0.09703703704,0.08444444444,0.06814814814,0.0651851852,0.0608,0.059199999999999996,0.0525925926]

print(corrcoef(x,y))

file1.close()
file3.close()
file2.close()
fileout.close()