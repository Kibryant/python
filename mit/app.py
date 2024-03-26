def main() -> None:
    cube = 27
    epsilon = 0.01
    low = 0
    high = cube
    guess = (high + low) / 2.0
    increment = 0.0001
    num_guesses = 0

    while abs(guess ** 3 - cube) >= epsilon:
        if guess ** 3 < cube:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2.0
        num_guesses += 1
    print(f'num_guesses = {num_guesses}')
    print(f'{guess} is close to the cube root of {cube}')

if __name__ == '__main__':
    tu = (1, "mit", True)
    print(tu[0])
    main()