import random

letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q'
          'r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H'
          'I','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols =['!','@','#','$','%','&','*','(',')']
numbers =['0','1','2','3','4','5','6','7','8','9']
password_list=[]
print("Welcome to password generate")
n_letters=int(input("How many letters you want in your password :"))
n_symbols=int(input("How many symbols you want in your password :"))
n_numbers=int(input("How many numbers you want in your password :"))

for char in range(1,n_letters+1):
    char=random.choice(letters)
    password_list.append(char)
    
    
    # password_list+=char
    
for char in range(1,n_symbols+1):
    char=random.choice(symbols)
    password_list+=char
for char in range(1,n_numbers+1):
    char=random.choice(numbers)
    password_list+=char

#print(password_list)    
random.shuffle(password_list)
#print(password_list)
end=""
for i in password_list:
    end+=i
print(end)    








