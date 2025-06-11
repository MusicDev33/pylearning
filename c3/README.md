# Challenge 3 - JSON Files and File Reading
You've been given a database, or at least something resembling it. They're two JSON files. You're going to need to be able to read those JSON files and turn them into Python dicts. Here's what you'll need to do:

- Create two functions, one for reading the users file into a dict and one for reading the location map into a dict
- Create another function for doing the following
  - Taking the username you input into the script
  - Grabbing the data you need from the other files (you'll call the other functions to do this)
  - Printing the data in the same exact format you did in Challenge 2

So running `python3 main.py sbennett` will give

```
Sophie Bennett
  Username: sbennett
  Location: London, UK
```

This one is going to be much more open-ended than the first 2 challenges. There are actually a few ways to solve this one, though for now, avoid classes. We'll get to those. Also, you'll have a main function and the 3 functions I talked about above. These don't have to be the only functions. If you find it beneficial to write more, go ahead.
