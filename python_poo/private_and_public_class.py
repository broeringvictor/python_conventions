class PrivatePublicClass:
    """
    In Python, unlike languages such as C# and Java, there isn't a strict
    keyword like `private` or `public` to enforce attribute visibility from outside the class.

    Instead, Python uses naming conventions to indicate the intended use and visibility:
    - A single leading underscore (_variable): This is a convention to indicate that
      an attribute or method is intended for internal use (sometimes referred to as "protected").
      It's a hint to other programmers, but it doesn't prevent access.
    - A double leading underscore (__variable): This triggers "name mangling". Python
      internally changes the name of the attribute to _ClassName__variableName, making it
      harder to access directly from outside the class. This is the closest Python gets
      to a "private" member by convention.

    This class demonstrates these conventions.
    """
    def __init__(self):
        """
        Initializes the class with a public attribute and a "private" attribute.
        """
        self.public_attribute = "I am public and can be accessed directly."
        self.__private_attribute = "I am 'private' due to the double underscore."
        self._internal_use_attribute = "I am for internal use (conventionally 'protected')."

        print(f"PrivatePublicClass instance created.")
        print(f"  - public_attribute: '{self.public_attribute}'")
        print(f"  - _internal_use_attribute: '{self._internal_use_attribute}' (accessible, but conventionally internal)")
        # We can access __private_attribute inside the class
        print(f"  - __private_attribute (inside class): '{self.__private_attribute}'")


    def display_public_info(self):
        """
        A public method that can be called from outside the class.
        """
        print(f"From display_public_info: Public attribute is '{self.public_attribute}'")

    def __private_method(self):
        """
        This method is "private" due to the double leading underscore.
        It's intended to be used only internally by the class.
        """
        return "This is a result from a 'private' method."

    def use_private_method(self):
        """
        A public method that calls the "private" method internally.
        """
        internal_result = self.__private_method()
        print(f"From use_private_method: {internal_result}")
        print(f"From use_private_method: Accessing private attribute: '{self.__private_attribute}'")

    def get_private_attribute_value(self):
        """
        This is a "getter" method, providing controlled access
        to the value of the "private" attribute.
        """
        return self.__private_attribute

    def set_private_attribute_value(self, new_value: str):
        """
        This is a "setter" method, providing controlled modification
        of the "private" attribute.
        """
        print(f"Setting __private_attribute from '{self.__private_attribute}' to '{new_value}' via setter.")
        self.__private_attribute = new_value

# --- Using the Class ---
print("--- Creating an instance of PrivatePublicClass ---")
obj = PrivatePublicClass()

print("\n--- Accessing Public Attributes and Methods ---")
# Public attributes are directly accessible
print(f"Direct access to public_attribute: {obj.public_attribute}")
obj.display_public_info()

print("\n--- Accessing 'Protected' Attributes (Convention) ---")
# Attributes with a single leading underscore are accessible,
# but the underscore signals they are for internal use.
print(f"Direct access to _internal_use_attribute: {obj._internal_use_attribute}")
obj._internal_use_attribute = "Changed internal use attribute" # Possible, but might break class internals
print(f"Modified _internal_use_attribute: {obj._internal_use_attribute}")


print("\n--- Attempting to Access 'Private' Attributes and Methods Directly ---")
# Attributes or methods starting with a double underscore (e.g., __private_attribute)
# are subject to 'name mangling'. Python changes their names to _ClassName__attributeName
# to make them harder to access directly from outside the class.
# This effectively makes them 'private' by convention, not by strict enforcement.

try:
    print(obj.__private_attribute)
except AttributeError as e:
    print(f"Error accessing obj.__private_attribute directly: {e}")

try:
    obj.__private_method()
except AttributeError as e:
    print(f"Error calling obj.__private_method() directly: {e}")

print("\n--- Accessing 'Private' Attributes via Getter/Setter Methods ---")
# The common and recommended way to interact with "private" data is through public methods (getters/setters).
private_val = obj.get_private_attribute_value()
print(f"Value from get_private_attribute_value(): {private_val}")

obj.set_private_attribute_value("New private value set by setter")
private_val_after_set = obj.get_private_attribute_value()
print(f"Value after set_private_attribute_value(): {private_val_after_set}")

print("\n--- Calling a Public Method that Uses 'Private' Members Internally ---")
obj.use_private_method()

print("\n--- Understanding Name Mangling (For Demonstration Only) ---")
# You *can* still access name-mangled attributes if you know the mangled name.
# This is generally discouraged as it breaks encapsulation.
# The mangled name is _ClassName__attributeName
try:
    print(f"Accessing via mangled name (discouraged): {obj._PrivatePublicClass__private_attribute}")
    mangled_method_result = obj._PrivatePublicClass__private_method()
    print(f"Calling mangled method (discouraged): {mangled_method_result}")
except AttributeError as e:
    print(f"Error accessing mangled name (should not happen if class name is correct): {e}")

print("\n--- End of Study ---")
