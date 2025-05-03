# mapping of coin to dollar
coin_values = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}
def normalize_coin_name(name):
    if name.endswith("ies"):
        return name[:-3] + "y"  # "pennies" -> "penny"
    elif name.endswith("s"):
        return name[:-1]  # "nickels" -> "nickel"
    return name

def parse_input(sentence):
    sentence = sentence.replace(" and", "")  # Remove "and" from sentence
    words = sentence.split()  # Split sentence into words
    total = 0.0

    # Loop through words in pairs (quantity, coin)
    for i in range(0, len(words), 2):
        try:
            quantity = int(words[i])  # Convert quantity to integer
            coin = normalize_coin_name(words[i + 1])  # Normalize coin name
            if coin in coin_values:
                total += quantity * coin_values[coin]  # Add value to total
            else:
                print(f"Warning: Unknown coin type '{coin}'")
        except ValueError:
            print(f"Error: Invalid quantity '{words[i]}'. Must be a number.")
            return None
    return round(total, 2)

if __name__ == "__main__":
    input_sentence = input("Enter a coin sentence: ")
    dollar_amount = parse_input(input_sentence)
    if dollar_amount is not None:
        print(f"${dollar_amount:.2f}")