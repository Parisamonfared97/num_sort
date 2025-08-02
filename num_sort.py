#تا وقتی کاربر 0 وارد نکرده عدد دریافت کند
#در یک لیست قرار دهد
#میانگین اعداد زوج دریافتی چاپ شود

num_list=[]
while True:
    num_input=int(input("Please Enter Your Number:"))
    if num_input==0:
        break
    else:
        num_list.append(num_input)
adade_zoj=list(filter(lambda num: num%2==0,num_list))
avg=sum(adade_zoj)/len(adade_zoj)
print("Average Number is :",avg)