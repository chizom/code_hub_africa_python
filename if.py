age_limit = 18
print('Welcome to CodeBeer')
users_age = input('How old are you to drink beer?: ')
users_age = int(users_age)

if users_age == 25:
    print('You can drink beer, and you just won a coupon')
elif users_age > age_limit:
        print('You can drink beer now :)')
else:
    print('You cannot drink beer with us')
