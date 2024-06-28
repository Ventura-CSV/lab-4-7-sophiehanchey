def main():
    numbers = []
    previousinput
    
    while True:
        currentinput = int(input('Please enter a number: '))
        
        numbers.append(currentinput)

        if(currentinput>previousinput):
            break
        else:
            previousinput = currentinput
            
    

    ########################################
    # Do not delete the return statement
    ########################################
    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()
