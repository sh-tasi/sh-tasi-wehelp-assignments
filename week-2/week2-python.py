import sys
def calculate(min,max):
    sum=0
    for n in range(min,max+1):
        sum=sum+n
    print(sum)
calculate(1,3)
calculate(4,8)

def avg(data):
    n=(data["count"])
    x=0
    for i in range(0,n):
        x=x+data["employees"][i]["salary"]
    y=x//n
    print(y)
    return(y)

avg({
    "count":3,
    "employees":[{
        "name":"John",
        "salary":30000
    },{
        "name":"Bob",
        "salary":60000
    },{
        "name":"Jenny",
        "salary":50000
    }
    ]
})
# def maxProduct(nums): 取得最大值&第二大值
#     x=len(nums)
#     t=-float('inf')
#     t2=-float('inf')
#     for i in (nums):
#         if i > t:
#             t=i
        
#     for i in (nums):
#         if t>i>t2:
#             t2=i
       
          
#     anser=t*t2
#     print(anser)
#     return(t*t2)
  
#   def maxProduct(nums): 解法2-取得最大值&第二大值
    #     t=-float('inf')
    # t2=-float('inf')
    # for i in (nums) :
    #   if i>t :
    #       t2=t;
    #        t=i;
    #     else :
            
    #         if i>t2 :
    #            t2=i;
    # t3=t*t2
    # print(t3) 
def maxProduct(nums):        #取得相乘最大值
    t2=-float('inf')          #t2為無窮小
    t=0                       #設一個t的變數
    i=0                      
    x=0
    long=len(nums)     
    while i<long:              # i取出nums中的數字
        y=nums[i] 
        i2=0                  #重製i2迴圈
        while i2<long:
            x=nums[i2]
         
            if i != i2 :        #避免取出相同元素之數字 
                        t=x*y;                                              
                        if  t>t2:
                                    t2=t;
            i2=i2+1 

        i=i+1
    print(t2)
  
       



maxProduct([5,20,2,6])
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2

def twoSum(nums, target):
    x=len(nums)
    i=0
    y=0   
    while i<x:
        y=y-y+(nums[i])
        m=0
        t=0
        while m<x :
                t=t-t+(nums[m])
                if y+t==target and i!=m:
                    print([i,m])
                    return([i,m])
                else:
                   m=m+1
        i=i+1 
    print("None")
    return(None)     
result=twoSum([2,11,7,15],9)

def maxZeros(nums):
    y=0  #假定一個值放入i作為判斷用
    y2=0 #假定最長的累積數量
    for i in (nums):
        t=i
        if t==0 :
            y=y+1           
        else :          
            if y2>y: #當遇到1的時後，如果已經存放的最長值大於目前累積的，就將累積的歸零，保留最長的
                y=0
            else :
                y2=y  #如果累積的比較長，就存放進去y2，並歸0
                y=0  
    #處裡最後一個是0，剛好又是最長累積的時候                        
    if y>y2:
            y2=y
    print(y2)
    return(y2)
maxZeros([0, 1, 0, 0]) #  2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) #4
maxZeros([1, 1, 1, 1, 1]) # 0
maxZeros([0, 0, 0, 1, 1]) # 3



