def find_value_of_x(data, target="x"):
    # Traverse the dictionary
    if isinstance(data, dict):
        for key, value in data.items():
            if key == '<program>':
                # We are looking for a list under '<program>'
                for item in value:
                    # Look for '<variable_declaration>' in the item
                    if isinstance(item, dict) and '<variable_declaration>' in item:
                        # Inside '<variable_declaration>', look for '<identifier>'
                        identifier = item['<variable_declaration>'].get('<identifier>', None)
                        if identifier == target:
                            # Found x, now get the value from '<expression>'
                            expression = item['<variable_declaration>'].get('<expression>', {})
                            return expression.get('<digit>', None)  # Get the value of the digit
    return None  # Return None if x is not found

# Example usage
data = {'<program>': [{'<variable_declaration>': {'<identifier>': 'x', '<expression>': {'<digit>': '456'}}}]}
result = find_value_of_x(data)
print(result)  # Expected output: 5


