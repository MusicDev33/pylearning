# Challenge 5 - Modules and the Runway
You can't put Python into one file forever; you'll need to modularize your code to keep it from becoming a twisted spaghetti mess. This is going to be the last challenge before the project, so it's going to be a bit more involved. We're going to do the following:

- Write a database
- Write a commandline interface

The whole package will be a program that we use to create new users or locations from the command line, though we'll be reading them from the command line too.

There will be code written for you already. We're going to be using UUIDs, and we'll be using indexes. Indexes are a way of mapping values to other values, just like any other map. Indexes allow us to retrieve data in a simpler way (or typically a faster way) from databases. This is going to be feel obtuse in this conrtived example, but in the real world, these are the kind of gymnastics you have to do to retrieve data.

## Your Task
I've written the location part of the database. You need to write the user part of the database. Then, we're going to have two modes for our program: read and write. Let's look at an example of each.

### Read
`python3 main.py -r username`

This will read our user from the database (or tell us they don't exist), and print all their data in a pretty format. We don't care to see the ID, but we do want to see the location (though you'll need to convert it to the human-readable form). For example, if we run `python3 main.py -r kmartin`, we want it to show that she's from Sydney, Australia!

### Write
`python3 main.py -w "Firstname Lastname" "City, Country"`

Note the `-w` flag. That will denote that we're in write mode! When we get this information, here's what we'll do:
- Automatically create a username from the first and last name. If you look at the data for Kleo Martin, you'll see the format.
- If the username already exists, spit out an error
- If the city does not exist, create it
- With everything else finished, add the user to the database
