import random


upper_case_letter1= chr(random.randint(65,90))
upper_case_letter2= chr(random.randint(65,90))
lower_case_letter1= chr(random.randint(97,122))
lower_case_letter2= chr(random.randint(97,122))
random_int1 = chr(random.randint(48,57))
random_int2 = chr(random.randint(48,57))
special_char1 = chr(random.randint(33,47))
special_char2 = chr(random.randint(60,64))

password = str(upper_case_letter1+upper_case_letter2+lower_case_letter1+lower_case_letter2+random_int1+random_int2+special_char1+special_char2) 
print(password)