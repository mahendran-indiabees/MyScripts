# MyScripts
MyScripts

You can use the following Groovy regex pattern to ensure that a string starts and ends with characters and allows the hyphen symbol within the string:

```groovy
^[a-zA-Z]+(?:-[a-zA-Z]+)*$
```

This pattern ensures that the string starts with a letter, followed by zero or more occurrences of a hyphen followed by a letter. It allows hyphens within the string but not at the beginning or end.
