# --- oop_study.py ---

from typing import Any, List # Import List and Any for type hinting

class StudyClassPoo: # PascalCase for class names
    """
    In Python, it's a common practice (a convention, really) to include a
    DocString like this at the beginning of a class, module, or function.
    This particular class is just a straightforward example for studying
    Object-Oriented Programming (OOP) concepts in Python.
    """

    # Class Attribute:
    # Shared by all instances of the class.
    # It's accessed using the class name (StudyClassPoo.instance_counter)
    # or through an instance (self.instance_counter, though modifying it
    # via self might create an instance attribute with the same name, shadowing the class one).
    instance_counter: int = 0

    # The __init__ method is a special method called a constructor.
    # It's automatically called when you create a new instance (object) of the class.
    # Its primary purpose is to initialize the instance variables (attributes) of the object.
    # 'self' refers to the instance of the class that is being created.
    def __init__(self, initial_value: str, numeric_id: int):
        """
        Initializes a new instance of StudyClassPoo.

        Args:
            initial_value (str): A string value to assign to an instance attribute.
            numeric_id (int): An integer value to represent an ID for the instance.
        """
        # Instance attributes are specific to each object.
        # They are defined here using 'self.attribute_name'.
        self.text_attribute: str = "This is a default text attribute"
        self.list_attribute: List[Any] = [10, 20, 30] # Each instance gets its own list
        self.custom_value: str = initial_value   # 'initial_value' is passed when creating an object
        self.identifier: int = numeric_id      # 'numeric_id' is also passed during object creation

        StudyClassPoo.instance_counter += 1 # Increment the class attribute
        print(f"StudyClassPoo object (ID: {self.identifier}) created. Custom Value: '{self.custom_value}'.")
        print(f"Total instances created so far: {StudyClassPoo.instance_counter}")

    # Methods are functions defined inside a class.
    # They operate on the data (attributes) of an instance of the class.
    # The first parameter of an instance method is always 'self'.
    def display_greeting(self) -> str: # snake_case for method names
        """
        Returns a simple greeting string.
        This method demonstrates a basic action an object can perform.
        """
        return f"Hello from StudyClassPoo object with ID {self.identifier}!"

    def get_custom_value(self) -> str:
        """
        Returns the value of the 'custom_value' attribute.
        This is a common pattern for accessing an object's state (getter method).
        """
        return self.custom_value

    def add_to_list(self, item_to_add: Any) -> None:
        """
        Adds a new item to the 'list_attribute'.
        This method modifies the object's state.

        Args:
            item_to_add (Any): The item to be added to the list.
        """
        self.list_attribute.append(item_to_add)
        # The print statement below is for demonstration; in many applications,
        # methods might just perform the action and not print directly.
        print(f"Item '{item_to_add}' added to list for object ID {self.identifier}. Current list: {self.list_attribute}")

    def get_instance_info(self) -> str:
        """
        Returns a string containing information about several attributes of the instance.
        Demonstrates methods can work with multiple attributes.
        """
        return (f"Instance Info (ID: {self.identifier}):\n"
                f"  Custom Value: {self.custom_value}\n"
                f"  Text Attribute: {self.text_attribute}\n"
                f"  List Attribute: {self.list_attribute}")

    # Special Method __str__
    # Defines the "official" string representation of an object.
    # Called by str(object) and implicitly by print(object).
    def __str__(self) -> str:
        """
        Returns a user-friendly string representation of the StudyClassPoo instance.
        """
        return f"<StudyClassPoo Instance | ID: {self.identifier}, Custom Value: '{self.custom_value}'>"

# --- Using the Class ---

# Classes are blueprints -> They don't perform actions themselves.
# We need to create an 'instance' or 'object' of the class to use its attributes and methods.

print("--- Creating Instances ---")
# Creating an instance (object) of StudyClassPoo:
# This will call the __init__ method with the provided arguments.
study_object1 = StudyClassPoo(initial_value="My First Object", numeric_id=101)
study_object2 = StudyClassPoo(initial_value="Another Instance", numeric_id=202)

print("\n--- Accessing Class Attribute ---")
# Accessing the class attribute (shared among all instances)
print(f"Value of class attribute 'instance_counter' (accessed via class): {StudyClassPoo.instance_counter}")
# You can also access it via an instance, but be careful if you try to assign to it via an instance.
print(f"Value of class attribute 'instance_counter' (accessed via study_object1): {study_object1.instance_counter}")


print("\n--- Calling Methods on Instances ---")
# Calling methods on the instance:
greeting_message1 = study_object1.display_greeting()
print(greeting_message1)

greeting_message2 = study_object2.display_greeting()
print(greeting_message2)

print("\n--- Using the __str__ Method ---")
# When you print an object, Python looks for a __str__ method.
print(study_object1) # Calls study_object1.__str__()
print(study_object2) # Calls study_object2.__str__()

print("\n--- Accessing Instance Attributes ---")
# Accessing attributes of an instance:
print(f"Object 1 Text Attribute: {study_object1.text_attribute}")
print(f"Object 1 Custom Value (via getter): {study_object1.get_custom_value()}")
print(f"Object 1 Identifier: {study_object1.identifier}")

print(f"Object 2 Custom Value (via getter): {study_object2.get_custom_value()}")
print(f"Object 2 Identifier: {study_object2.identifier}")

print("\n--- Modifying an Instance Attribute through a Method ---")
print(f"Object 1 List before adding: {study_object1.list_attribute}")
study_object1.add_to_list("New Item Alpha")
study_object1.add_to_list(999)
# print(f"Object 1 List after adding: {study_object1.list_attribute}") # This print is now part of add_to_list

# Note that changes to study_object1 do not affect study_object2,
# as they are independent instances with their own 'list_attribute'.
print(f"Object 2 List (should be unchanged by Object 1's actions): {study_object2.list_attribute}")
study_object2.add_to_list("New Item Beta")

print("\n--- Using the get_instance_info Method ---")
print(study_object1.get_instance_info())
print(study_object2.get_instance_info())

print("\n--- Demonstrating Instance Independence ---")
# Modifying an attribute directly (generally, prefer methods if there's logic involved)
study_object1.text_attribute = "Changed text for Object 1"
print(f"Object 1 Text Attribute after change: {study_object1.text_attribute}")
print(f"Object 2 Text Attribute (should be original): {study_object2.text_attribute}")

print("\n--- End of Study ---")
