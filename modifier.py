import os
import datetime
import numpy as np


'''
(1) set system time to 2017-08-08
(2) do the following
    git init
    git add -A
    git commit -m "first commit"
    git remote add origin https://github.com/Leo-2000/Tmp.git
    git push -u origin master   (Leo-2000, abc123@)
(3) set system time back
(4) run script
'''

path = 'test.txt'


def ModifyFile(path):
    string = 'Hello World'
    with open(path, 'a') as file:
        file.writelines(string)
        file.writelines('\n')
        
def PassTime(date):
    while True: 
        m = np.random.randint(low=1000, high=7000)
        new = date + datetime.timedelta(minutes=m)
        if new.weekday()<5:
            break
    return new
    
def Datetime2String(date):
    return date.strftime('%Y-%m-%d %H:%M:%S')
    
def ModifyProject(date, iteration):
    for idx in range(iteration):
        ModifyFile(path)
        date = PassTime(date)
        os.environ['GIT_COMMITTER_DATE'] = Datetime2String(date)
        os.environ['GIT_AUTHOR_DATE'] = Datetime2String(date)
        os.system('git add -A')
        commit_msg = '"' + str(idx) + '"'
        os.system('git commit -m ' + commit_msg)
        
        
    
def TestDatatime():
    d1 = datetime.datetime(2017, 8, 8, 9, 27, 35)
    string = d1.strftime('%Y-%m-%d %H:%M:%S')
    print(string)
    
    m = np.random.randint(low=1000, high=7000)
    d2 = d1 + datetime.timedelta(minutes=m)
    string = d2.strftime('%Y-%m-%d %H:%M:%S')
    print(string)
    
    if d2.weekday()<5:
        print('weekday')
    else:
        print('weekend')

if __name__=='__main__':
    
    #ModifyFile(path)
    #InitGitProject('https://github.com/Leo-2000/Test.git','2017-08-08 09:27:35')
    
    date = datetime.datetime(2017, 8, 8, 9, 27, 35)
    ModifyProject(date=date, iteration=10)
    
    