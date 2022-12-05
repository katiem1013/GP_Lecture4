# activity 3
def f_to_c(f_temp):
      c_temp = (f_temp - 32) * (5/9)
      return c_temp

print(f_to_c(100))

# activity 2
import random

safe_code = []

while len(safe_code) < 3:
      code = random.randint(3,12)
      if code not in safe_code:
            safe_code.append(code)

codes_cracked = 0

while codes_cracked < len(safe_code):
      for code in safe_code:
            print("you must enter a pair of numbers that divide to %d" % code)
            try:

                  player_number_1 = float(input("Enter number: "))
                  player_number_2 = float(input("Enter number: "))
                  result = player_number_1//player_number_2
                  if result == code:
                        print("yay?")
                        codes_cracked += 1

            except ValueError:
                  print("Not a number.")
                  break;

            except ZeroDivisionError:
                  print("Can't divide by zero.")

            except:
                  print("Can't do that.")

else:
      print("you have opened the safe")