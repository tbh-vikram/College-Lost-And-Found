# College Lost and Found Matcher

## Project Statement

The **College Lost and Found Matcher** is a simple Python-based system
designed to help students report, store, and find lost or found items
within a college campus.

The program allows users to report an item they have found by entering
its name, colour, and location. These details are stored in a text file
so that the information remains available when the program is run again.

If a student has lost an item, they can enter the item's name, colour,
and the place where they lost it. The program compares these details
with the stored found items and displays possible matches. Each matching
detail is given one point, and an item with all three matching details
is treated as an exact match and removed from the found-items list.

The system also provides an option to display all currently reported
found items. File handling is used to store and retrieve the data, while
dictionaries are used to organize item information.

## Main Features

-   Report a lost item.
-   Report a found item.
-   Compare lost-item details with found items.
-   Display possible matches based on matching details.
-   Identify an exact match when all three details match.
-   Remove an item after an exact match is found.
-   Display all currently stored found items.
-   Store data permanently using a text file.
-   Handle an empty or missing data file.

## Technologies Used

-   Python
-   Dictionaries
-   Conditional statements
-   Loops
-   Functions
-   File handling
-   String operations

## Data Stored

For every found item, the program stores:

1.  Item name
2.  Colour
3.  Location

The information is saved in `found_items.txt` using the `|` symbol to
separate the fields.

## Objective

The main objective of this project is to provide a simple and practical
way for college students to manage lost and found items and quickly
identify possible matches.
