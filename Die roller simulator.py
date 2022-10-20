import random as r

def die_side():
    nums = "123456"
    random_num = r.sample(nums,1)
    random_num = int(''.join(random_num))

    return random_num


def run(random_die):
    roll = True
    
    while roll:

        print(f"The selected die number is: {random_die}")

        user_input = input("roll again(y/n)? ").lower()

        if user_input == 'y':
            random_die = die_side()
        else:
            roll = False
    

if __name__ == '__main__':

    die_num = die_side()
    run(die_num)