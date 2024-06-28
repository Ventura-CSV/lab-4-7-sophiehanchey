def main():
    numbers = []
    
    while True:
        currentinput = int(input('Please enter a number: '))
        numbers.append(currentinput)
        print(numbers[-2])

        if(currentinput>numbers[-2] or len(numbers) < 1):
            break
            
    

    ########################################
    # Do not delete the return statement
    ########################################
    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()
