# Visualization for company stakeholders

#check loan status approved or not 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()
loan_status.plot(kind='bar')
plt.title('visualizing the companys record with respect to loan approvals')
plt.xlabel('Loan Status')
plt.ylabel('VALUES')
plt.show()

# Which is the region with the highest no. of loan approvals? lowest no. of loan approvals?

property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()
print(property_and_loan)
property_and_loan.plot(kind='bar',stacked=False)
plt.xlabel('Property Area')
plt.ylabel('Loan status')
plt.xticks(rotation=45)
plt.show()

#Overall which group has asked for higher loan services irrespective of the approval? Graduate or Non Graduate?
#Which group has had better approval to non approval ratio? Graduate or Non Graduate?
#Do the above conclusions make sense? Why

education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked = True)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.title('Expensive Education')
plt.xticks(rotation=45)

#Do Graduate people get approved a higher amount than their Non Graduate counterparts?
#What's the average amount of loan approved for Graduate? for Non Graduate? Is there a huge difference between the two?

graduate=data[data['Education']=='Graduate']
not_graduate=data[data['Education']=='Not Graduate']
graduate['LoanAmount'].plot(kind='density',label='Graduate')
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')

#Is there a correlation between 'ApplicantIncome' and 'LoanAmount'?(One way to know that is look at the line formed when you connect the scatter plot dots?)
#Is the 'TotalIncome' better related to the 'LoanAmount' than 'ApplicantIncome'? 

fig ,(ax_1,ax_2,ax_3) = plt.subplots(nrows=3, ncols=1,figsize=(20,20))
ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'])
ax_1.set(title='Applicant Income')
ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'])
ax_2.set(title='Coapplicant Income')
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
ax_3.scatter(data['TotalIncome'],data['LoanAmount'])
ax_3.set(title='Total Income')