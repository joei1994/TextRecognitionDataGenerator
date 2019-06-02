import random

th_letters = [chr(o) for o in range(ord('ก'), ord('ฮ')+1)]
digits = [chr(o) for o in range(ord('0'), ord('9')+1)]
n_lines = 200000

def rand_digit():
    return random.choice(digits)
def rand_letter():
    return random.choice(th_letters)

def main():
    with open('./dicts/th.txt', 'ab') as fid:
        for n in range(n_lines):
            n_first = random.choice([2,3])
            n_second = random.choice([3,4])

            if n_first > 2:
                first_ch = str(rand_digit())
                rest_chs = ''.join([rand_letter() for _ in range(n_first-1)])
                first_string = first_ch + rest_chs
            else:
                first_string = ''.join([random.choice(th_letters) for _ in range(n_first)])

            second_string = ''.join([random.choice(digits) for _ in range(n_second)])

            line = first_string + ' ' + second_string

            if n == n_lines - 1:
                line =  line + ' '
            else:
                line =  line + '\n'    

            fid.write(line.encode('UTF-8'))                
if __name__ == '__main__':
    main()