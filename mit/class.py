class Fraction(object):
    def __init__(self, num: int, denom: int) -> None:
        self.num = num
        self.denom = denom
    
    def __str__(self) -> str:
        return f"{self.num} / {self.denom}"

def main() -> None:
    fraction = Fraction(4, 3)
    print(fraction)

if __name__ == "__main__":
    main()