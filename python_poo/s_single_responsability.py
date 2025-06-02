class RegistrationSystem:
    """
    A class to handle user registration in a system.
    This class follows the Single Responsibility Principle (SRP) by focusing solely on user registration."""

    # Method to register a user
    def register(self, name: str, age: int) -> None:
        # Check if the input is valid
        if self.__validate_input(name, age):
            # If valid, register the user
            self.__register_user(name, age)
        else:
            # If invalid, handle the error
            self.__error_handle()

    # Private method to validate input
    def __validate_input(self, name: str, age: int) -> bool:
        # Returns True if name is a string and age is an integer
        return isinstance(name, str) and isinstance(age, int) # 1: Validates data types

    # Private method to register the user in the "database"
    def __register_user(self, name: str, age: int) -> None:
        # Simulates database access
        print("Accessing the database...") # 2: Simulates database interaction
        # Simulates user registration
        print(f"Registering user {name}, age {age}")

    # Private method to handle errors
    def __error_handle(self) -> None:
        # Prints an error message for invalid data
        print("Invalid data") # 3: Handles input validation errors

# Create an instance of RegistrationSystem
system = RegistrationSystem()
# Register a user
system.register("Victor", 28)
