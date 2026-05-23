class RomanConverter:
    def __init__(self):
       
        self.value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def int_to_roman(self, num: int) -> str:
        """Converts an integer to a Roman numeral string."""
        roman_numeral = ""
        for value, symbol in self.value_map:
            # While the number is greater than or equal to the current value
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral

if __name__ == "__main__":
    converter = RomanConverter()
    
    test_number = 1994
    result = converter.int_to_roman(test_number)
    
    print(f"Integer: {test_number}")
    print(f"Roman Numeral: {result}")






