import string
import random

Firstname=input('What is your firstname ')
Lastname=input('Please input your lastname ')
email=input('what is your email ')

def pw_gen(size = 5, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

print("This is your password: "+Firstname[:2]+pw_gen()+{Lastname[-2:].upper()})

statement = input("Are you satisfied with this password? ")


if statement == "yes":
    print('HERE ARE YOUR DETAILS')
    print("Your Fullname is: "+ Firstname+" "+Lastname)
    print("And your email is: "+ email)

elif statement == "no":
   passcode =  input("INPUT YOUR DESIRED PASSWORD ")
   if len(passcode)>7:
       print('HERE ARE YOUR DETAILS')
       print("Your Fullname is: " + Firstname + " " + Lastname)
       print("And your email is: " + email)
   else:
       print("kindly input a password greater than or equal to seven(7) characters")
