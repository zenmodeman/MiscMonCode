from mpmath import mp
import random

NUM_MONS = 1025

def get_pi_digits(n=(NUM_MONS*3)+1):

  #First 2 characters are "3.", and the remaining digits are n-1
  #so we need 2 + (n-1) = n+1
  mp.dps = n + 1

  pi_digits = str(mp.pi).replace(".", "")
  return pi_digits



pi_digits = get_pi_digits()

# print(pi_digits[900:910])



def get_nth_pi_string(n=1):
  pi_digits = get_pi_digits()
  starting_index = (n - 1) * 3
  return pi_digits[starting_index:starting_index + 3]


def get_next_strings(start_string=1, num_strings=10):
  pi_digits = get_pi_digits()
  for i in range(start_string, start_string + num_strings + 1):
    starting_digit = (i - 1) * 3
    print(i, pi_digits[starting_digit:starting_digit + 3])

#337 -> Lunatone [Hoopa - 720]
#338 -> Solrock [Hitmonlee - 106]

# print(get_nth_pi_string(323))

#The current number up to which I have learned.
WORKING_STRING = 390

def perform_single_quiz(min_string = 1, max_string = WORKING_STRING, terminating_score = 10):
   num_correct = 0 
   num_attempts = 0
   while num_correct < terminating_score:
      rand_string_num = random.randrange(min_string, max_string + 1)
      answer = str(get_nth_pi_string(rand_string_num))
      user_input = input(f"Enter the value of string #{rand_string_num}: ")
      if answer == user_input:
         num_correct += 1
         print(f"Correct answer! Your score is now {num_correct}")
      else:
         print(f"Incorrect, the correct answer is {answer}")
      num_attempts +=1
   print(f"You have finished the quiz with {num_correct} answers correct in {num_attempts} attempts!")


def perform_sequence_quiz(min_digit = 1, max_digit = 1000, step = 10, runs = 3):
    pi_digits = get_pi_digits()
    min_init_digit = min_digit + step
    max_init_digit = max_digit - step

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
   # print(perform_sequence_quiz())
   #Using this block of code as a sanity check of the previous digits as the most recent one
   get_next_strings(340, 10)
   # perform_single_quiz() 



