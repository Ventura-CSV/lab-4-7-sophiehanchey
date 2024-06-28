def main():
    numbers = []
    currentinput = int(input('Enter a number: '))
    previousinput = currentinput
    
    while currentinput <= previousinput:
        currentinput = int(input('Please enter another number: '))
        
        numbers.append(currentinput)
        previousinput = currentinput

    ########################################
    # Do not delete the return statement
    ########################################
    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()
