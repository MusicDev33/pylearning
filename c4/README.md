# Challenge 4 - Parsing Text
Notice how we just deal with a lot of text data? Yeah. That's a lot of what programming is. All we've done so far is parse text, but now it's time to spit out some text! In this challenge, we're going to parse a log file!

We need to turn the log file into something a little more readable to humans. Here's the thing: we do care about successful events, or at least we like to see them, but we mostly care about errors, and kind of care about warnings. It also appears the log file got messed up somehow, so there are duplicate entries too. Nothing a bit of programming can't solve!

We're going to parse `logs.txt` and then put the results in `parse.txt`. We're going to group all the errors in `parse.txt`, with errors at the top, warnings below that, and successes at the bottom. Let's do it like this:

```
===== ERRORS =====
Deadlock detected - transaction rolled back (table='orders')
# ...

===== WARNINGS =====
Partial insert in 'inventory' table - 2 out of 5 rows succeeded
# ...

===== SUCCESSES =====
Inserted 1 row into 'users' table (id=101, name="John Doe", email="john@example.com")
# ...
```
