# README
---
# Introduction
This is a test based adventure game. To keep things clean and
organized there are certain standards which you must adhere too.
Failure to adhere to these standards will result in messy, code.
Please adhere to any and all standards.

# Standards
* Spaces not tabes. (If you hit tab in VCS it will put 4 spaces)
* snake_case for everything. Execption being classes whcih are in 
PascalCase
* Functions for everything. Exec should no more than 10 lines.
* Markdown for long amounts of text such as this one.
* When naming functions you are to put to domain of the function
before the actuale purpose. For example `text_display` rather than
`display_text`. That way you can skim the code for "text" functions.
* Text files that are meant to be displayed in-game should have 2
blank lines (newlines) at the end of it.
* A newline should end every single file. Sometimes more.
* All inputs should be `> `. Don't forget the space.
* When accepting input rember to capitlize the input.
* When a character dies in the game, print the game over screen
and type `quit()`
* There should be 2 newlines after a function is defined
* Put `ERROR: ` before all error messages.
* When you put a message put `===` around it if it is a long 
message and `===== [msg] =====` if it is short.

*As always this is a countious standard, and may change.*

# Crash Corse - Python Functions
In order to create a function you need to define it. You do this 
with `def`. For example `def [function_name]`. After you declare
the fucntion name you must put the options in parenshesis. These 
options work just like parenthesis, and will be set when you call
the function. Eg. `def display_text(color, size)`. At the end of
it all don't forget to colon, and the subsuquent code. Varibales
made in a function are called "local variables". You cannot use
a variable from one function in a different function. The exception
is "global variables". You can declare a global variable as `global
[variable]`. Did you know the best prefix for a global variable
is `#? I joke, but only a little. Don't use global variables if you
can avoid it.

## Example
```python
def speak(msg):
    print(msg)
```

# Crash Corse - Mardown
## Introduction
Markdown is a system designed to be read and written from the
terminal. Rather than clicking "B" on your screen you type
`**[msg]**` to bold. This is useful because it means that messages
without WYSIWYG (what you see is what you get) formating, can 
still be neat, and interperted by a wide variety of machines.

## Rules
(This is a table in Markdown.)
| Symbol        | Meaning         |
|---------------|-----------------|
| #             | Title           |
| ##            | Sub-Title etc   |
| *             | Unordered List  |
| *[msg]*       | Italics         |
| **[msg]**     | Bold            |
| `[msg]`       | Inline Code     |
| ```[msg]```   | Code Block      |
| 1, 2, etc     | Numbered List   |
| [msg]([link]) | Embed Links     |
| ---           | Line            |
