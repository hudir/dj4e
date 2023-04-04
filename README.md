# dj4e
Learn Django -  https://www.dj4e.com/
 3-html
 4-css

https://hudir.pythonanywhere.com/


 # Wrong and unknown Q&A

## Which of the following files in a Django application most closely captures the notion of "View"?
 - templates/polls/main.html

## Which file represents the "Controller" aspect of a Django application?
 - It is not as simple as that (42)

## What does the built-in Django template tag "spaceless" do?
 - Removes whitespace between HTML tags. This includes tab characters and newlines.
 Only space between tags is removed – not space between tags and text. In this example, the space around Hello won’t be stripped:

{% spaceless %}
    <strong>
        Hello
    </strong>
{% endspaceless %}

## What does the built-in Django template filter "length" do?
Returns the length of the value. This works for both strings and lists.

## What is the built-in Django template filter to count the number of words in a string? [_____]
wordcount
Returns the number of words.

## Looking at the Django built-in template and filter documentation, the author seems to have a pet named "Joel". What kind of animal is their pet?
"Joel is a slug"

## What does the Django built-in template tag forloop.counter represent in a Django template?
forloop.counter	The current iteration of the loop (1-indexed)
forloop.counter0	The current iteration of the loop (0-indexed)

## In Object Oriented Programming, what is another name for the attributes of an object?
fields

## Which of the following is NOT a good synonym for "class" in Python?
direction

## Which of the following is rarely used in Object Oriented Programming?
 Destructor


## In the class django.views.generic.list.ListView, which of the following methods is called earliest in the process?

 get_template_names()