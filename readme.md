The Factory Design Pattern is a creational pattern that deals with object creation without having to explicitly specify the exact class of the object that will be created. It provides a central place to decide what kind of object to create and how to create it.

Here's a breakdown of how it works:

Concept:

Factory Class: A Factory class defines an interface for creating objects but lets subclasses decide which class to instantiate. The Factory class hides the logic of object creation from the client code (the code that uses the objects).
Concrete Classes: These are the actual classes that implement the product (the object being created). They inherit from a common interface or abstract class that defines the methods the product implements.
Client Code: The client code interacts with the factory, requesting a specific type of object using the interface or abstract class. The factory then creates the appropriate concrete class and returns it to the client.


Benefits:
-----------

Loose Coupling: The client code doesn't need to know the specific classes of the objects it's using. This makes the code more flexible and easier to maintain. You can change the implementation of the concrete classes without affecting the client code.
Code Reusability: The factory class can encapsulate the logic for creating objects, which can be reused by different parts of your code.
Subtyping: You can easily introduce new types of objects by creating new concrete classes that inherit from the common interface or abstract class.



Note:-
after.py and before.py was taken example from "https://www.youtube.com/watch?v=s_4ZrtQs8Do"