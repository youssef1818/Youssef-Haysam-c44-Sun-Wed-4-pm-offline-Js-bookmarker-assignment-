def armstrong_check ():
    print ("====================================")
    print ("====== Armstrong number check ======")
    print ("====================================")

    armst_num=input('Enter the number you want to check: ')
    while str.isdigit(armst_num) is False:
        armst_num=input('Please Enter a valid integer: ')
    i=0
    sum=0
    arm_list=[]
    power=int(len(armst_num))
    for i in  range(len(armst_num)):
        digit=int(armst_num[i])
        arm_list.append(digit)  
        sum=digit**power+sum
    if sum == int(armst_num):
        print('The Number is an Armstrong number')
    else:
        print ('The number is not an Armstrong number')



armstrong_check()
