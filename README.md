# MyScripts
MyScripts
You can use the following Groovy regex pattern to ensure that a string does not start or end with special characters while allowing the '-' (hyphen) symbol within the string:

```groovy
^(?![-!@#$%^&*()_+=[\]{};:'\"<>,./?\\|`~].*|.*[-!@#$%^&*()_+=[\]{};:'\"<>,./?\\|`~]$)[a-zA-Z0-9-]+$
```

This pattern utilizes negative lookahead assertions to ensure that the string does not start or end with special characters while allowing letters (both uppercase and lowercase), numbers, and the '-' symbol within the string.
