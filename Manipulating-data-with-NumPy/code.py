# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here

data = np.genfromtxt(path,delimiter =",",skip_header =1)

print("\nData: \n\n", data)
print("\nType of data: \n\n",type(data))

census = np.concatenate((new_record,data),axis = 0)





# --------------
#Code starts here
age = np.array(census[:,0])
max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)
print(age)
print(max_age)
print(min_age)
print(age_std)


# --------------
#Code starts here
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

print(len_0)
print(len_1)
print(len_2)
print(len_3)
print(len_4)

race_list = [len_0,len_1,len_2,len_3,len_4]

min_c = min(race_list)

minority_race = race_list.index(min_c)

print(minority_race)


# --------------
#Code starts here
senior_citizens = census[census[:,0]>60]
mask = senior_citizens > 60


working_hours_sum = senior_citizens.sum(axis=0)[6]

print(working_hours_sum)

senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)

avg_working_hours = working_hours_sum/ senior_citizens_len

print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1]>10]
low = census[census[:,1]<=10]

avg_pay_high = np.mean(high,axis=0)[7]

avg_pay_low = np.mean(low,axis=0)[7]

print(high)
print(low)
print(avg_pay_high)
print(avg_pay_low)


