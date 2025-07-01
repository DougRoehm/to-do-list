# Simple To Do List
def main():

    # initiate the to do list dictionary
    td_list = {}

    # user input to add items to list and ctrl-d to end list
    while True:
        try:
            item = input().upper()
        except EOFError:
            break
        else:
            if item in td_list:
                td_list[item] += 1 # will increment item already on list
            else:
                td_list[item] = 1 # will add item to list

    # Print list sorted by key
    for key, quantity in sorted(td_list.items()):
        print(quantity, key)

if __name__ == "__main__":
    main()

# It will allow a user to enter items on the list.
# They can press ctrl-d to exit entering items on the list.
# They can see a printout of the items on the list.
# They can remove items on the list.