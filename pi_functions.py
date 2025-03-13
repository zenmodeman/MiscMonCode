from mpmath import mp
import random

NUM_MONS = 1025

def get_pi_digits(n=NUM_MONS):

  #First 2 characters are "3.", and the remaining digits are n-1
  #so we need 2 + (n-1) = n+1
  mp.dps = n + 1

  pi_digits = str(mp.pi).replace(".", "")
  return pi_digits


pi_digits = get_pi_digits()

# print(pi_digits[900:910])



def get_nth_pi_string(n=1):
  pi_digits = get_pi_digits(NUM_MONS + 1)
  starting_index = (n - 1) * 3
  return pi_digits[starting_index:starting_index + 3]


def get_next_strings(start_string=1, num_strings=10):
  pi_digits = get_pi_digits(NUM_MONS + 1)
  for i in range(start_string, start_string + num_strings + 1):
    starting_digit = (i - 1) * 3
    print(i, pi_digits[starting_digit:starting_digit + 3])


# print(get_nth_pi_string(323))

def perform_digit_quiz(min_digit = 1, max_digit = 1008, step = 10, runs = 3):
    pi_digits = get_pi_digits()
    min_init_digit = min_digit + 10
    max_init_digit = max_digit - 10

    for i in range(runs):
       print(f"Starting run #{i+1} out of {runs} runs.")
       starting_digit = random.randrange(min_init_digit, max_init_digit+1)
       starting_idx = starting_digit - 1 
       forward_nums = pi_digits[starting_idx:starting_idx+step]
       forward_input = (input(f"Enter {step} forward digits of pi starting from digit #{starting_digit}: "))
       if str(forward_nums) == forward_input:
          print("Correct answer!")
       else:
          print(f"Incorrect. The correct answer is: {forward_nums}.")
       
       backward_nums = pi_digits[starting_idx:starting_idx-step:-1]
       backward_input = input(f"Enter {step} backward digits of pi starting from digit #{starting_digit}: ")
       if str(backward_nums) == backward_input:
          print("Correct answer!")
       else:
          print(f"Incorrect. The correct answer is: {backward_nums}.")

if __name__ == "__main__":
   print(perform_digit_quiz())
    



