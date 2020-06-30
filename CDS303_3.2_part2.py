import regex as re
import numpy as np
import csv

ID1 = 'BEGH'
ID2 = 'ABCEGH'
ID3 = 'ABCEFH'
ID4 = 'BCDEFGHL'
ID5 = 'ABEKH'
ID6 = 'BEFGHIK'
ID7 = 'ABDGH'
ID8 = 'ABDG'
ID9 = 'BDFG'
ID10 = 'CEF'
ID11 = 'ACEFH'
ID12 = 'ABEG'

list1 = [ID1,ID2,ID3,ID4,ID5,ID6,ID7,ID8,ID9,ID10,ID11,ID12]

# generates all possible non repeating patterns, and looks for hits on the list:
def func1(list,characters,minSupport):
    pattern = characters
    list2 = []
    pattern3 = ''
    counter = 0
    for i in range(1,len(pattern)):
        pattern2 = '+.*'+str(pattern[i])
        pattern3 = pattern3+pattern2
    pattern4 = str(pattern[0])+pattern3

   # print('ID | PAT | sequence')
    for i in range(0,len(list1)):
        match = re.findall(pattern4,list1[i],re.IGNORECASE)
        if match:

            list2.append([(i+1),pattern, list1[i]])
            #print(list2[counter])
            counter += 1
    #print('total matches = ', counter)
    return list2,counter

# 4size
def fun4(list,characters,minSupport):

    # print(' # | pattern | string | hits | permutation table position')
    superlist = []
    maxI = len(characters)
    kprime = 0
    permutationList = []
    for h in range(0, maxI):
        for i in range((h + 1), maxI):
            for j in range((i + 1), maxI):
                for k in range((j + 1), maxI):
                    result = func1(list1,str(characters[h]+characters[i]+characters[j]+characters[k]),minSupport)
                    #print(h, i, j, k)
                    #print(characters[h] + characters[i] + characters[j] + characters[k])
                    permutationList.append(characters[h]+characters[i]+characters[j]+characters[k])
                    if result[1]>=minSupport:
                        kprime += 1
                        superlist.append((kprime, result))

    return (superlist,permutationList)
# 3size
def fun3(list,characters,minSupport):

    # print(' # | pattern | string | hits | permutation table position')
    superlist = []
    maxI = len(characters)
    kprime = 0
    permutationList = []
    for h in range(0, maxI):
        for i in range((h + 1), maxI):
            for j in range((i + 1), maxI):
                    result = func1(list1,str(characters[h]+characters[i]+characters[j]),minSupport)
                    #print(h, i, j)
                    #print(characters[h] + characters[i] + characters[j] + characters[k])
                    permutationList.append(characters[h]+characters[i]+characters[j])
                    if result[1]>=minSupport:
                        kprime += 1
                        superlist.append((kprime, result))

    return (superlist,permutationList)
# 2 sizw
def fun2(list,characters,minSupport):

    # print(' # | pattern | string | hits | permutation table position')
    superlist = []
    maxI = len(characters)
    kprime = 0
    permutationList = []

    for h in range(0, maxI):
        for i in range((h + 1), maxI):
                    result = func1(list1,str(characters[h]+characters[i]),minSupport)
                    #print(h, i)
                    #print(characters[h] + characters[i])
                    permutationList.append(characters[h] + characters[i])
                    if result[1]>=minSupport:
                        kprime += 1

                        superlist.append((kprime, result))

    return (superlist,permutationList)
# 1 size
def fun1(list,characters,minSupport):

    # print(' # | pattern | string | hits | permutation table position')
    superlist = []
    maxI = len(characters)
    kprime = 0
    permutationList = []
    for h in range(0, maxI):
                    result = func1(list1,str(characters[h]),minSupport)
                    #print(h)
                    #print(characters[h] + characters[i] + characters[j] + characters[k])
                    permutationList.append(characters[h])
                    if result[1]>=minSupport:
                        kprime += 1
                        superlist.append((kprime, result))

    return (superlist,permutationList)

minSupport = 4
# c4
print('\n\n\n\n4\n')
fun = fun4(list1,'BEGH',0)
for i in range(0,len(fun)):
    print(fun[i])
with open('c4_2.csv','w',newline='') as f:
    writer1 = csv.writer(f,'excel')
    firstLine = []
    totalsLine = []
    listID = []

    for number1 in range(0,len(fun[0])):
        len2 = len(fun[0][number1])
        #for number2 in range(0,len(fun[0][0][1][0])-1):
            # only results with support greater than min sup
        take_letter = True
        totalsLine.append(fun[0][number1][1][1])
        elem = fun[0][number1][1][0]

        for elem2 in elem:
            # grab letter to make column names row ( for Ln table as opposed to the candidate table)
            if take_letter:
                firstLine.append(elem2[1])
                take_letter = False
            listID.append((elem2[0], elem2[1]))

            #for elem3 in elem2:


    writer1.writerow( fun[1] )
    arr4 = np.zeros(((len(list1), len(fun[1]))))
    arr = arr4.tolist()
    dict1={}
    for i in range(0,len(fun[1])):
        dict1[fun[1][i]] = i
    for i in range(0,len(listID)):
        a =listID[i][0]-1
        b = dict1[listID[i][1]]
        c = listID[i][1]
        arr[a] [b] = listID[i][1]

    #arr4(listID[0],dict[listID[1]]) = 1

    for row in arr:
        writer1.writerow(row)
    #print(arr.shape)
    writer1.writerow( totalsLine )

# l4
minSupport = 4
print('\n\n\n\n4\n')
fun = fun4(list1,'BEGH',6)
print(arr4)
for i in range(0,len(fun)):
    print(fun[i])
with open('l4_2.csv','w',newline='') as f:


    writer1 = csv.writer(f,'excel')
    # fistline takes only letters that surpassed the minSupport parameter
    firstLine = []
    totalsLine = []
    listID = []

    for number1 in range(0,len(fun[0])):
        len2 = len(fun[0][number1])
        #for number2 in range(0,len(fun[0][0][1][0])-1):
            # only results with support greater than min sup
        take_letter = True
        elem = fun[0][number1][1][0]

        for elem2 in elem:
            # grab letter to make column names row ( for Ln table as opposed to the candidate table)

            if len(elem) >= minSupport:
                listID.append((elem2[0], elem2[1]))
                if take_letter:
                    firstLine.append(elem2[1])
                    take_letter = False
                    totalsLine.append(fun[0][number1][1][1])

            #for elem3 in elem2:



    arr4 = np.zeros(((len(list1), len(firstLine))))
    arr = arr4.tolist()
    dict1={}
    for i in range(0,len(firstLine)):
        dict1[firstLine[i]] = i
    for i in range(0, len(listID)):
        a = listID[i][0] - 1
        b = dict1[listID[i][1]]
        c = listID[i][1]
        arr[a][b] = listID[i][1]


    # write csv section
    writer1.writerow(firstLine)
    for row in arr:
        writer1.writerow(row)
    #print(arr.shape)
    writer1.writerow( totalsLine )


# c3
print('\n\n\n\n3\n')
fun = fun3(list1,'BEGH',0)
for i in range(0,len(fun)):
    print(fun[i])
with open('c3_2.csv','w',newline='') as f:
    writer1 = csv.writer(f,'excel')
    firstLine = []
    totalsLine = []
    listID = []

    for number1 in range(0,len(fun[0])):
        len2 = len(fun[0][number1])
        #for number2 in range(0,len(fun[0][0][1][0])-1):
            # only results with support greater than min sup
        take_letter = True
        totalsLine.append(fun[0][number1][1][1])
        elem = fun[0][number1][1][0]

        for elem2 in elem:
            # grab letter to make column names row ( for Ln table as opposed to the candidate table)
            if take_letter:
                firstLine.append(elem2[1])
                take_letter = False
            listID.append((elem2[0], elem2[1]))

            #for elem3 in elem2:


    writer1.writerow( fun[1] )
    arr4 = np.zeros(((len(list1), len(fun[1]))))
    arr = arr4.tolist()
    dict1={}
    for i in range(0,len(fun[1])):
        dict1[fun[1][i]] = i
    for i in range(0,len(listID)):
        a =listID[i][0]-1
        b = dict1[listID[i][1]]
        c = listID[i][1]
        arr[a] [b] = listID[i][1]

    #arr4(listID[0],dict[listID[1]]) = 1

    for row in arr:
        writer1.writerow(row)
    #print(arr.shape)
    writer1.writerow( totalsLine )

# l3
print('\n\n\n\n3\n')
fun = fun3(list1,'BEGH',6)
for i in range(0,len(fun)):
    print(fun[i])
with open('l3_2.csv', 'w', newline='') as f:
    writer1 = csv.writer(f, 'excel')
    # fistline takes only letters that surpassed the minSupport parameter
    firstLine = []
    totalsLine = []
    listID = []

    for number1 in range(0, len(fun[0])):
        len2 = len(fun[0][number1])
        # for number2 in range(0,len(fun[0][0][1][0])-1):
        # only results with support greater than min sup
        take_letter = True

        elem = fun[0][number1][1][0]

        if len(elem) >= minSupport:
            totalsLine.append(fun[0][number1][1][1])
            for elem2 in elem:
                # grab letter to make column names row ( for Ln table as opposed to the candidate table)
                listID.append((elem2[0], elem2[1]))
                if take_letter:

                    if len(elem) >= minSupport:

                        if take_letter:
                            firstLine.append(elem2[1])
                            take_letter = False

            # for elem3 in elem2:

    arr4 = np.zeros(((len(list1), len(firstLine))))
    arr = arr4.tolist()
    dict1 = {}
    for i in range(0, len(firstLine)):
        dict1[firstLine[i]] = i
    for i in range(0, len(listID)):
        a = listID[i][0] - 1
        b = dict1[listID[i][1]]
        c = listID[i][1]
        arr[a][b] = listID[i][1]

    # write csv section
    writer1.writerow(firstLine)
    for row in arr:
        writer1.writerow(row)
    # print(arr.shape)
    writer1.writerow(totalsLine)


# c2
print('\n\n\n\n2\n')
fun = fun2(list1,'BEGH',0)
for i in range(0,len(fun)):
    print(fun[i])
print('\n\n\n\n4\n')
fun = fun4(list1,'BEGH',0)
for i in range(0,len(fun)):
    print(fun[i])
with open('c2_2.csv','w',newline='') as f:
    writer1 = csv.writer(f,'excel')
    firstLine = []
    totalsLine = []
    listID = []

    for number1 in range(0,len(fun[0])):
        len2 = len(fun[0][number1])
        #for number2 in range(0,len(fun[0][0][1][0])-1):
            # only results with support greater than min sup
        take_letter = True
        totalsLine.append(fun[0][number1][1][1])
        elem = fun[0][number1][1][0]

        for elem2 in elem:
            # grab letter to make column names row ( for Ln table as opposed to the candidate table)
            if take_letter:
                firstLine.append(elem2[1])
                take_letter = False
            listID.append((elem2[0], elem2[1]))

            #for elem3 in elem2:


    writer1.writerow( fun[1] )
    arr4 = np.zeros(((len(list1), len(fun[1]))))
    arr = arr4.tolist()
    dict1={}
    for i in range(0,len(fun[1])):
        dict1[fun[1][i]] = i
    for i in range(0,len(listID)):
        a =listID[i][0]-1
        b = dict1[listID[i][1]]
        c = listID[i][1]
        arr[a] [b] = listID[i][1]

    #arr4(listID[0],dict[listID[1]]) = 1

    for row in arr:
        writer1.writerow(row)
    #print(arr.shape)
    writer1.writerow( totalsLine )

# l2
print('\n\n\n\n2\n')
fun = fun2(list1,'BEGH',6)
for i in range(0,len(fun)):
    print(fun[i])
with open('l2_2.csv', 'w', newline='') as f:
    writer1 = csv.writer(f, 'excel')
    # fistline takes only letters that surpassed the minSupport parameter
    firstLine = []
    totalsLine = []
    listID = []

    for number1 in range(0, len(fun[0])):
        len2 = len(fun[0][number1])
        # for number2 in range(0,len(fun[0][0][1][0])-1):
        # only results with support greater than min sup
        take_letter = True

        elem = fun[0][number1][1][0]

        if len(elem) >= minSupport:
            totalsLine.append(fun[0][number1][1][1])
            for elem2 in elem:
                # grab letter to make column names row ( for Ln table as opposed to the candidate table)
                listID.append((elem2[0], elem2[1]))
                if take_letter:

                    if len(elem) >= minSupport:

                        if take_letter:
                            firstLine.append(elem2[1])
                            take_letter = False

            # for elem3 in elem2:

    arr4 = np.zeros(((len(list1), len(firstLine))))
    arr = arr4.tolist()
    dict1 = {}
    for i in range(0, len(firstLine)):
        dict1[firstLine[i]] = i
    for i in range(0, len(listID)):
        a = listID[i][0] - 1
        b = dict1[listID[i][1]]
        c = listID[i][1]
        arr[a][b] = listID[i][1]

    # write csv section
    writer1.writerow(firstLine)
    for row in arr:
        writer1.writerow(row)
    # print(arr.shape)
    writer1.writerow(totalsLine)

# c1
print('\n\n\n\n1\n')
fun = fun1(list1,'BEGH', 0)
for i in range(0,len(fun)):
    print(fun[i])
with open('c1_2.csv','w',newline='') as f:
    writer1 = csv.writer(f,'excel')
    firstLine = []
    totalsLine = []
    listID = []

    for number1 in range(0,len(fun[0])):
        len2 = len(fun[0][number1])
        #for number2 in range(0,len(fun[0][0][1][0])-1):
            # only results with support greater than min sup
        take_letter = True
        totalsLine.append(fun[0][number1][1][1])
        elem = fun[0][number1][1][0]

        for elem2 in elem:
            # grab letter to make column names row ( for Ln table as opposed to the candidate table)
            if take_letter:
                firstLine.append(elem2[1])
                take_letter = False
            listID.append((elem2[0], elem2[1]))

            #for elem3 in elem2:


    writer1.writerow( fun[1] )
    arr4 = np.zeros(((len(list1), len(fun[1]))))
    arr = arr4.tolist()
    dict1={}
    for i in range(0,len(fun[1])):
        dict1[fun[1][i]] = i
    for i in range(0,len(listID)):
        a =listID[i][0]-1
        b = dict1[listID[i][1]]
        c = listID[i][1]
        arr[a] [b] = listID[i][1]

    #arr4(listID[0],dict[listID[1]]) = 1

    for row in arr:
        writer1.writerow(row)
    #print(arr.shape)
    writer1.writerow( totalsLine )

# l1
print('\n\n\n\n1\n')
fun = fun1(list1,'BEGH',6)
for i in range(0,len(fun)):
    print(fun[i])
with open('l1_2.csv','w',newline='') as f:


    writer1 = csv.writer(f,'excel')
    # fistline takes only letters that surpassed the minSupport parameter
    firstLine = []
    totalsLine = []
    listID = []

    for number1 in range(0,len(fun[0])):
        len2 = len(fun[0][number1])
        #for number2 in range(0,len(fun[0][0][1][0])-1):
            # only results with support greater than min sup
        take_letter = True

        elem = fun[0][number1][1][0]

        if len(elem) >= minSupport:
            totalsLine.append(fun[0][number1][1][1])
            for elem2 in elem:
                # grab letter to make column names row ( for Ln table as opposed to the candidate table)
                listID.append((elem2[0], elem2[1]))
                if take_letter:

                    if len(elem) >= minSupport:

                        if take_letter:
                            firstLine.append(elem2[1])
                            take_letter = False


            #for elem3 in elem2:



    arr4 = np.zeros(((len(list1), len(firstLine))))
    arr = arr4.tolist()
    dict1={}
    for i in range(0,len(firstLine)):
        dict1[firstLine[i]] = i
    for i in range(0, len(listID)):
        a = listID[i][0] - 1
        b = dict1[listID[i][1]]
        c = listID[i][1]
        arr[a][b] = listID[i][1]


    # write csv section
    writer1.writerow(firstLine)
    for row in arr:
        writer1.writerow(row)
    #print(arr.shape)
    writer1.writerow( totalsLine )

