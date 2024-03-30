/*
Challenge: Book Inventory System

Create a program for managing a bookstore's inventory.

 The program should have the following features:

An object-oriented model using classes and inheritance.
A class that implements an interface for books.
A class that overrides an inherited method to provide specific functionality for different types of books.
An instance of a class that is initialized with data from a file containing information about available books.
A method that demonstrates the use of a loop to display information about all books in the in

*/





// Define an interface for books
abstract class Book {
  void displayInfo();
}

// Define a superclass for all books
class BookBase implements Book {
  String title;
  String author;
  double price;

  BookBase(this.title, this.author, this.price);

  @override
  void displayInfo() {
    print('Title: $title, Author: $author, Price: $price');
  }
}

// Define subclasses for different types of books
class Fiction extends BookBase {
  String genre;

  Fiction(String title, String author, double price, this.genre)
      : super(title, author, price);

  @override
  void displayInfo() {
    super.displayInfo();
    print('Genre: $genre');
  }
}

class NonFiction extends BookBase {
  String topic;

  NonFiction(String title, String author, double price, this.topic)
      : super(title, author, price);

  @override
  void displayInfo() {
    super.displayInfo();
    print('Topic: $topic');
  }
}

// Define a method to read data from a file and initialize instances of classes
List<Book> initializeFromFile(String fileName) {
  List<Book> books = [];

  // Read data from the file and initialize instances of classes
  // For demonstration purposes, we'll simulate reading from a file
  // In a real application, you would read actual data from a file
  books.add(Fiction('The Great Gatsby', 'F. Scott Fitzgerald', 15.99, 'Classic'));
  books.add(Fiction('To Kill a Mockingbird', 'Harper Lee', 12.99, 'Classic'));
  books.add(NonFiction('Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 20.99, 'History'));
  books.add(NonFiction('Educated: A Memoir', 'Tara Westover', 18.99, 'Autobiography'));

  return books;
}

// Define a method that demonstrates the use of a loop to display information about all books
void displayAllBooks(List<Book> books) {
  print('Inventory:');
  for (var book in books) {
    book.displayInfo();
    print('---');
  }
}

void main() {
  // Initialize instances of classes with data from a file
  List<Book> inventory = initializeFromFile('books.txt');

  // Display information about all books in the inventory
  displayAllBooks(inventory);
}
