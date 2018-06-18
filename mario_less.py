#print Mario piramid_less comfortable

def main():
#get positive integer from a user (the height) greater than 0 smaller then 23
    import cs50

    while True:
        print("height:", end="")
        height=cs50.get_int()
        if height>0 and height<=23:
            break

    width=height-1 #create a variable to remember amount of spaces to print in each row
    h=2 #create a variable to remember the amount of # to print in each row

    #iterate over each row
    for i in range(height):

        #print spaces in each row
        print(" "*width, end="")

        #print # in each row
        print("#"*h, end="")

        h+=1 #increment amount of # to print in the next row
        width-=1 #decrement amout of spaces to print in the next row
        print ("") #print a new line

if __name__ == "__main__":
    main()

