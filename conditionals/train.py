# we need build based user amount we need show the seat type
#for this we use switch case 
#1st we need tack input form user 
seat_type = input(f"enter u r seat type general/ac/sleeper/luxuery: ").lower()

match seat_type:
     case "sleeper":
          print(f"sleeper ")
     case "general":
          print(f"no reservation ")
     case "ac":
          print(f"confly ac ")
     case "luxuery":
          print(f"full of confort ")
     case _:
          print(f"invalied seat type")