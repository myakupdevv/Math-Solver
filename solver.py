def solve_math_operation(operation):
    try:
        result = eval(operation)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    operation = input("Enter a math operation: ")
    print(f"Result: {solve_math_operation(operation)}")
