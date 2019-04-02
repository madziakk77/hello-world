#!/usr/bin/python

row_1 = [1, 11, 31, 41]
row_2 = [2, 12, 32]
row_3 = [3]
row_4 = [4]
row_5 = [5]
row_6 = [6]

row_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
row_20 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 10]
row_30 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 20]
row_40 = [31, 32, 33, 34, 35, 36, 37, 38, 39, 30]
row_50 = [41, 42, 43, 44, 45, 46, 47, 48, 49, 40]
col_1 = [1, 11, 21, 31, 41]
col_2 = [2, 12, 22, 32, 42]
col_3 = [3, 13, 23, 33, 43]
col_4 = [4, 14, 24, 34, 44]
col_5 = [5, 15, 25, 35, 45]
col_6 = [6, 16, 26, 36, 46]
col_7 = [7, 17, 27, 37, 47]
col_8 = [8, 18, 28, 38, 48]
col_9 = [9, 19, 29, 39, 49]
col_0 = [10, 20, 30, 40]

sum_10=0
sum_20=0
sum_30=0
sum_40=0
sum_50=0
sum_1=0
sum_2=0
sum_3=0
sum_4=0
sum_5=0
sum_6=0
sum_7=0
sum_8=0
sum_9=0
sum_0=0

def ile(liczba, row_xx):
    ile_razem=0
    for licznik_row in row_xx:
        if liczba == licznik_row:
            ile_razem=ile_razem+1
    return ile_razem

for loop_1 in row_1:
    sum_10_1=ile(loop_1,row_10)
    sum_20_1=ile(loop_1,row_20)
    sum_30_1=ile(loop_1,row_30)
    sum_40_1=ile(loop_1,row_40)
    sum_50_1=ile(loop_1,row_50)
    sum_1_1=ile(loop_1,col_1)
    sum_2_1=ile(loop_1,col_2)
    sum_3_1=ile(loop_1,col_3)
    sum_4_1=ile(loop_1,col_4)
    sum_5_1=ile(loop_1,col_5)
    sum_6_1=ile(loop_1,col_6)
    sum_7_1=ile(loop_1,col_7)
    sum_8_1=ile(loop_1,col_8)
    sum_9_1=ile(loop_1,col_9)
    sum_0_1=ile(loop_1,col_0)
    for loop_2 in row_2:
        if loop_1 <> loop_2:
            sum_10_2=ile(loop_2,row_10)
            sum_20_2=ile(loop_2,row_20)
            sum_30_2=ile(loop_2,row_30)
            sum_40_2=ile(loop_2,row_40)
            sum_50_2=ile(loop_2,row_50)
            sum_1_2=ile(loop_2,col_1)
            sum_2_2=ile(loop_2,col_2)
            sum_3_2=ile(loop_2,col_3)
            sum_4_2=ile(loop_2,col_4)
            sum_5_2=ile(loop_2,col_5)
            sum_6_2=ile(loop_2,col_6)
            sum_7_2=ile(loop_2,col_7)
            sum_8_2=ile(loop_2,col_8)
            sum_9_2=ile(loop_2,col_9)
            sum_0_2=ile(loop_2,col_0)
            for loop_3 in row_3:
                if loop_1 <> loop_3:
                    if loop_2 <> loop_3:
                        sum_10_3=ile(loop_3,row_10)
                        sum_20_3=ile(loop_3,row_20)
                        sum_30_3=ile(loop_3,row_30)
                        sum_40_3=ile(loop_3,row_40)
                        sum_50_3=ile(loop_3,row_50)
                        sum_1_3=ile(loop_3,col_1)
                        sum_2_3=ile(loop_3,col_2)
                        sum_3_3=ile(loop_3,col_3)
                        sum_4_3=ile(loop_3,col_4)
                        sum_5_3=ile(loop_3,col_5)
                        sum_6_3=ile(loop_3,col_6)
                        sum_7_3=ile(loop_3,col_7)
                        sum_8_3=ile(loop_3,col_8)
                        sum_9_3=ile(loop_3,col_9)
                        sum_0_3=ile(loop_3,col_0)
                        for loop_4 in row_4:
                            if loop_1 <> loop_4:
                                if loop_2 <> loop_4:
                                    if loop_3 <> loop_4:
                                        sum_10_4=ile(loop_4,row_10)
                                        sum_20_4=ile(loop_4,row_20)
                                        sum_30_4=ile(loop_4,row_30)
                                        sum_40_4=ile(loop_4,row_40)
                                        sum_50_4=ile(loop_4,row_50)
                                        sum_1_4=ile(loop_4,col_1)
                                        sum_2_4=ile(loop_4,col_2)
                                        sum_3_4=ile(loop_4,col_3)
                                        sum_4_4=ile(loop_4,col_4)
                                        sum_5_4=ile(loop_4,col_5)
                                        sum_6_4=ile(loop_4,col_6)
                                        sum_7_4=ile(loop_4,col_7)
                                        sum_8_4=ile(loop_4,col_8)
                                        sum_9_4=ile(loop_4,col_9)
                                        sum_0_4=ile(loop_4,col_0)
                        for loop_5 in row_5:
                            if loop_1 <> loop_5:
                                if loop_2 <> loop_5:
                                    if loop_3 <> loop_5:
                                        if loop_4 <> loop_5:
                                            sum_10_5=ile(loop_5,row_10)
                                            sum_20_5=ile(loop_5,row_20)
                                            sum_30_5=ile(loop_5,row_30)
                                            sum_40_5=ile(loop_5,row_40)
                                            sum_50_5=ile(loop_5,row_50)
                                            sum_1_5=ile(loop_5,col_1)
                                            sum_2_5=ile(loop_5,col_2)
                                            sum_3_5=ile(loop_5,col_3)
                                            sum_4_5=ile(loop_5,col_4)
                                            sum_5_5=ile(loop_5,col_5)
                                            sum_6_5=ile(loop_5,col_6)
                                            sum_7_5=ile(loop_5,col_7)
                                            sum_8_5=ile(loop_5,col_8)
                                            sum_9_5=ile(loop_5,col_9)
                                            sum_0_5=ile(loop_5,col_0)
                                            for loop_6 in row_6:
                                                if loop_1 <> loop_6:
                                                    if loop_2 <> loop_6:
                                                        if loop_3 <> loop_6:
                                                            if loop_4 <> loop_6:
                                                                if loop_5 <> loop_6:
                                                                    sum_10_6=ile(loop_6,row_10)
                                                                    sum_20_6=ile(loop_6,row_20)
                                                                    sum_30_6=ile(loop_6,row_30)
                                                                    sum_40_6=ile(loop_6,row_40)
                                                                    sum_50_6=ile(loop_6,row_50)
                                                                    sum_1_6=ile(loop_6,col_1)
                                                                    sum_2_6=ile(loop_6,col_2)
                                                                    sum_3_6=ile(loop_6,col_3)
                                                                    sum_4_6=ile(loop_6,col_4)
                                                                    sum_5_6=ile(loop_6,col_5)
                                                                    sum_6_6=ile(loop_6,col_6)
                                                                    sum_7_6=ile(loop_6,col_7)
                                                                    sum_8_6=ile(loop_6,col_8)
                                                                    sum_9_6=ile(loop_6,col_9)
                                                                    sum_0_6=ile(loop_6,col_0)
                                                                    sum_10=sum_10_1+sum_10_2+sum_10_3+sum_10_4+sum_10_5+sum_10_6
                                                                    sum_20=sum_20_1+sum_20_2+sum_20_3+sum_20_4+sum_20_5+sum_20_6
                                                                    sum_30=sum_30_1+sum_30_2+sum_30_3+sum_30_4+sum_30_5+sum_30_6
                                                                    sum_40=sum_40_1+sum_40_2+sum_40_3+sum_40_4+sum_40_5+sum_40_6
                                                                    sum_50=sum_50_1+sum_50_2+sum_50_3+sum_50_4+sum_50_5+sum_50_6
                                                                    sum_1=sum_1_1+sum_1_2+sum_1_3+sum_1_4+sum_1_5+sum_1_6
                                                                    sum_2=sum_2_1+sum_2_2+sum_2_3+sum_2_4+sum_2_5+sum_2_6
                                                                    sum_3=sum_3_1+sum_3_2+sum_3_3+sum_3_4+sum_3_5+sum_3_6
                                                                    sum_4=sum_4_1+sum_4_2+sum_4_3+sum_4_4+sum_4_5+sum_4_6
                                                                    sum_5=sum_5_1+sum_5_2+sum_5_3+sum_5_4+sum_5_5+sum_5_6
                                                                    sum_6=sum_6_1+sum_6_2+sum_6_3+sum_6_4+sum_6_5+sum_6_6
                                                                    sum_7=sum_7_1+sum_7_2+sum_7_3+sum_7_4+sum_7_5+sum_7_6
                                                                    sum_8=sum_8_1+sum_8_2+sum_8_3+sum_8_4+sum_8_5+sum_8_6
                                                                    sum_9=sum_9_1+sum_9_2+sum_9_3+sum_9_4+sum_9_5+sum_9_6
                                                                    sum_0=sum_0_1+sum_0_2+sum_0_3+sum_0_4+sum_0_5+sum_0_6
                                                                    for i1 in [sum_10, sum_20, sum_30, sum_40, sum_50]:
                                                                        if i1 == 4:
                                                                            for i2 in [sum_10, sum_20, sum_30, sum_40, sum_50]:
                                                                                if i2 == 2:
                                                                                    for i3 in [sum_10, sum_20, sum_30, sum_40, sum_50]:
                                                                                        if i3 == 0:
                                                                                            for i4 in [sum_10, sum_20, sum_30, sum_40, sum_50]:
                                                                                                if i4 == 0:
                                                                                                    for i5 in [sum_10, sum_20, sum_30, sum_40, sum_50]:
                                                                                                        if i5 == 0:
                                                                                                            print loop_1, loop_2, loop_3, loop_4, loop_5, loop_6, sum_10, sum_20, sum_30, sum_40, sum_50


print "poza loop_1"
print "loop_1-5:", loop_1, loop_2, loop_3, loop_4, loop_5
print  "sumy=", sum_10, sum_20, sum_30, sum_40, sum_50
