# importing the modules
import menu
import asserting
import time

# creating user lists
lst = []
change_history = []

# We read the user's input
n = int(input("What is the length of your list?: "))

print("Enter elements: ")
for i in range(0, n):
    e = int(input())
    lst.append(e)


# We put the initial list as our base for the list of lists that records
# all changes we have made.
change_history.append(lst[:])




# Running the menu until user quits

while True:
    # we store the user's choice in q
    q = menu.start(lst)

    if q == "0":
        break
    
    elif q == "U" or q == "u":
        # We pop the last list we have created and print the last list from the list of lists. This acts like an "undo"
        # Also we will not undo if we have don't have any other lists in the stack apart from the initial list

        if len(change_history) > 1:
            change_history.pop()

            # here we print the last element of the list of lists
            print(change_history[-1])

    else:
        # Running the functions + assertion based on choice
        asserting.options(lst, q)

        # We append a *copy* of the last lst because otherwise all other lists we have added so far will also change
        change_history.append(lst[:])


    # waiting 0.6s for the menu to pop up for a smoother user experience :d
    time.sleep(0.6)
