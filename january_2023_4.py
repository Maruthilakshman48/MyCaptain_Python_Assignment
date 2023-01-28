# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 20:51:05 2023

@author: Admin
"""

import csv
 
def write_info_csv(info_list):
     with open('student_info.csv', 'a', newline='')as csv_file:
         writer = csv.writer(csv_file)
          
         if csv_file.tell() == 0:
             writer.writerow(["Name", "age", "Contact Number", "E-Mail ID"])
             
             writer.writerow(info_list)
             
if __name__ == '__main__':
  condition = True
  student_num = 1 
  
  while(condition):
     student_info =input("enter student information for student#{} in the following format(Name age contact_number e-mail_id):".format(student_num))

     
     # split
     student_info_list = student_info.split(' ')
     
     print("\nthe entered information is -\nname: {}\nage: {}\nContact_number: {}\ne-mail id: {}"
           .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))   
     
     condition_check = input("is entered information correct? (yes/no):")
      
     if choice_check == "yes":

         write_into_csv(student_info_list)
         condition_check = input("enter (yes/no) if you want to enter information for another student:")
    if condition_check == "yes" :
          condition = True
          student_num = student_num + 1
      
elif condition_check == "no":
          condition = False
elif choice_check == "no" :
        
        print("\nplease re-enter the values!")
