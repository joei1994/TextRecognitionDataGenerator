import argparse
import random
import numpy as np
from tqdm import tqdm

th_letters = [chr(o) for o in range(ord('ก'), ord('ฮ')+1) if chr(o) not in 'ฤฦ']
digits = [chr(o) for o in range(ord('0'), ord('9')+1)]
n_lines = 200000

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-rm',
        '--random_mode',
        type=str, 
        default = 'mix'
    )
    
    return parser.parse_args()

def rand_digit():
    return random.choice(digits)
def rand_letter():
    return random.choice(th_letters)
def rand_mix(digit_weight, letter_weight):
    is_digit = random.choices([True, False], weights=[digit_weight, letter_weight])[0]
    if is_digit:
        return random.choice(digits)
    else:
        return random.choice(th_letters)

def get_first(n_first, rand_mode):
    if rand_mode == 'mix':            
        return ''.join([rand_mix(digit_weight=0.3, letter_weight=0.7) for _ in range(n_first)])
    else:
        if n_first > 2:
            first_ch = str(rand_digit())
            rest_chs = ''.join([rand_letter()for _ in range(n_first-1)])
            return first_ch + rest_chs
        else:
            return ''.join([rand_letter() for _ in range(n_first)])
        
def get_second(n_second, rand_mode):
    if rand_mode == 'mix':
        return ''.join([rand_mix(digit_weight=0.6, letter_weight=0.4) for _ in range(n_second)])
    elif rand_mode == 'digit':
        return ''.join([rand_digit() for _ in range(n_second)])
    elif rand_mode == 'letter':
        return ''.join([rand_letter() for _ in range(n_second)])

def get_line(n_first, n_second, rand_mode = 'mix'):
    first_string = get_first(n_first, rand_mode)
    second_string = get_second(n_second, rand_mode)

    return first_string + ' ' + second_string

def main():
    args = parse_arguments()
    with open('./dicts/th.txt', 'ab') as fid:
        for n in tqdm(range(n_lines)):
            n_first = random.choice([2,3])
            n_second = random.choice([3,4])

            line = get_line(n_first, n_second, args.random_mode)

            if n == n_lines - 1:
                line =  line + ' '
            else:
                line =  line + '\n'    

            fid.write(line.encode('UTF-8'))                
if __name__ == '__main__':
    main()