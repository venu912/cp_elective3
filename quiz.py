# Write the function bestQuiz(a), which takes a rectangular 2d list of numbers that represents a gradebook, where each column represents a quiz, and each row represents a student, and each value represents that student's score on that quiz (except -1 indicates the student did not take the quiz). For example:
#   a = [ [ 88,  80, 91 ],
#         [ 68, 100, -1 ]
#       ]
# This list indicates that student0 scored 88 on quiz0, 80 on quiz1, and 91 on quiz2. Also, student1 scored 68 on quiz0, 100 on quiz1, and did not take quiz2. The function returns the quiz with the highest average. In this case, quiz0 average is 78, quiz1 average is 90, and quiz2 average is 91 (since we ignore the -1). Thus, quiz2 is the best, and so the function returns 2 in this case. You are not responsible for malformed input, except you should return None if there are no quizzes. Also, resolve ties in favor of the lower quiz number. Here is a test function for you:

# def bestQuiz(l):
#       # a=l[0][0]+l[1][0]
#       # b=l[0][1]+l[1][1]
#       # c=l[0][2]+l[1][2]
#       print(l)
#       a=[]
#       j=0
#       for i in range(len(l)):
#             if(l[i][j]==-1):
#                   l[i][j]=0
#             if(l[i][j+1]==-1):
#                   l[i][j+1]=0
#             a.append(l[i][j]+l[i+1][j])   
#       print(a)
#       return a
#print(bestQuiz([ [ 88,  80, 91 ],[ 68, 100, -1 ]]))

def bestQuiz(l):
    # Your  code goes ehre...
      sums=[]
      for i in range(len(l[0])):
            sum=0
            count=0
            for j in range(len(l)):
                  if(l[j][i]!=-1):
                        sum+=l[j][i]
                        count+=1
            if(count!=0):
                  avg=sum/count
                  sums.append(avg)
      if(len(sums)==0):
            return None
      m=sums.index(max(sums))
      return m
#print(bestQuiz([ [ 88,  80, 91 ],[ 68, 100, -1 ]]))
                  
                  
            
def testBestQuiz():
    print('Testing bestQuiz()...', end='')
    a = [ [ 88,  80, 91 ],
          [ 68, 100, -1 ]]
    assert(bestQuiz(a) == 2)
    a = [ [ 88,  80, 80 ],
          [ 68, 100, 100 ]]
    assert(bestQuiz(a) == 1)
    a = [ [88, -1, -1 ],
          [68, -1, -1 ]]
    assert(bestQuiz(a) == 0)
    a = [ [-1, -1, -1 ],
          [-1, -1, -1 ]]
    assert(bestQuiz(a) == None)
    print('All test cases passed...!')
