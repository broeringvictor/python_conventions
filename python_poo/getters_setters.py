# --- my_class_encapsulation_study.py ---

class MyClass:
    """
    In Python, encapsulation, the bundling of data (attributes) and methods
    that operate on the data within a single unit (a class), is often
    achieved using "private" attributes (by convention, prefixed with double
    underscores like __private_value) and public methods (getters and setters)
    to control access to these attributes.

    Type hints are crucial here as they clearly define the expected types for
    method parameters and return values, improving code readability and
    maintainability.
    """

    def __init__(self, value: int):
        """
        Initializes the class with a "private" attribute.
        The type hint `value: int` specifies that the initial value must be an integer.

        Args:
            value (int): The initial integer value for the private attribute.
        """
        # __private_value is conventionally private due to the double underscore.
        # It's good practice to initialize attributes with the correct type.
        if not isinstance(value, int):
            raise TypeError("Initial value must be an integer.")
        self.__private_value: int = value
        print(f"MyClass instance created with initial private value: {self.__private_value}")

    def getter_value(self) -> int:
        """
        Getter method to retrieve the current value of the "private" attribute.
        The type hint `-> int` clearly indicates that this method will return an integer.

        Returns:
            int: The current value of the __private_value attribute.
        """
        print(f"Getter: Retrieving __private_value: {self.__private_value}.")
        return self.__private_value

    def setter_value(self, new_value: int) -> None:
        """
        Setter method to update the "private" attribute.
        The type hint `new_value: int` specifies that the new value must be an integer.
        The return type hint `-> None` indicates that this method does not return any value;
        its purpose is to modify the object's state.

        This method includes validation to ensure the new value is of the correct type.

        Args:
            new_value (int): The new integer value to set for the __private_value attribute.

        Raises:
            ValueError: If new_value is not an integer.
        """
        if not isinstance(new_value, int):
            # It's common to raise a TypeError for incorrect types,
            # but ValueError is also acceptable if the value itself is problematic.
            raise ValueError("Invalid value: new_value must be an integer.")
        
        print(f"Setter: Setting __private_value from {self.__private_value} to {new_value}.")
        self.__private_value = new_value

# Example usage, as you provided
if __name__ == "__main__":
    print("--- Creating MyClass object ---")
    try:
        my_obj = MyClass(10)
    except TypeError as e:
        print(f"Error during object creation: {e}")
        # Exit or handle if object creation fails
        my_obj = MyClass(0) # Fallback for demonstration

    print("\n--- Using Getter ---")
    current_value = my_obj.getter_value()
    print(f"Value from getter: {current_value}")  # Should print 10 (or 0 if initial creation failed)

    print("\n--- Using Setter with a valid value ---")
    my_obj.setter_value(20)       # Should update the value to 20
    current_value_after_set = my_obj.getter_value()
    print(f"Value from getter after valid set: {current_value_after_set}")  # Should print 20

    print("\n--- Using Setter with an invalid value ---")
    try:
        print("Attempting to set value to a string...")
        my_obj.setter_value("not an int")  # type: ignore # Should raise ValueError
    except ValueError as e:
        print(f"Caught expected error: {e}")

    final_value = my_obj.getter_value()
    print(f"Final value in object: {final_value}") # Should still be 20

    print("\n--- Attempting to create MyClass with invalid initial type ---")
    try:
        invalid_obj = MyClass("wrong type") # type: ignore
    except TypeError as e:
        print(f"Caught expected error during creation: {e}")

    print("\n--- End of MyClass Demonstration ---")
