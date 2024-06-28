def main():
    numbers = []
    
    while True:
        currentinput = int(input('Please enter a number: '))
        numbers.append(currentinput)

        #checks that the list is long enough to have a previous value
        if(len(numbers)>1):
            # print(numbers[-2]) -> checks what the previous value was
            if(currentinput > numbers[-2]):
                break
    
    #excludes final number
    del numbers[-1]
    

    ########################################
    # Do not delete the return statement
    ########################################
    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()
