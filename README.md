# AirBnB clone - MySQL

This directory is home to all files and Sub-directories needed for successful completion of the 'MySQL' AirBnB_clone_v2 project provided by ALX Africa to its Software Engineering program.

<h3> GENERAL REQUIREMENTS: </h3>

```(1) PYTHON SCRIPTS```

	->	Allowed editors:
		    vi, vim, emacs
	->	All files will be interpreted/compiled on Ubuntu 20.04 LTS using:
		    python3 (version 3.8.5)
	->	All files should end with a new line
	->	The first line of all files should be exactly:
		    #!/usr/bin/python3
	->	A README.md file, at the root of the folder of the project, is mandatory
	->	Code should use:
		     pycodestyle (version 2.8.*)
	->	All files must be executable
	->	The length of files will be tested using wc
	->	All  modules should have a documentation:
		     python3 -c 'print(__import__("my_module").__doc__)'
	->	All  classes should have a documentation:
		     python3 -c 'print(__import__("my_module").MyClass.__doc__)'
	->	All  functions (inside and outside a class) should have a documentation:
		     python3 -c 'print(__import__("my_module").my_function.__doc__)'
		     python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
	->	A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

```(2) PYTHON UNIT TESTS```

	->	Allowed editors:
		    vi, vim, emacs
	->	All files should end with a new line
	->	All test files should be inside a folder tests
	->	The testing module to be used has to be:
			unittest
	->	All test files should be python files:
			extension: .py
	->	All test files and folders should start with test_
	->	The file organization in the tests folder should be the same as the project's:
		    Example: for models/base_model.py, unit tests must be in:
			tests/test_models/test_base_model.py
		    Example: for models/user.py, unit tests must be in:
			tests/test_models/test_user.py
	->	All tests should be executed by using any of commands:
		    python3 -m unittest discover tests
		    python3 -m unittest tests/test_models/test_base.py
	->	All  modules should have a documentation:
		     python3 -c 'print(__import__("my_module").__doc__)'
	->	All  classes should have a documentation:
		     python3 -c 'print(__import__("my_module").MyClass.__doc__)'
	->	All  functions (inside and outside a class) should have a documentation:
		     python3 -c 'print(__import__("my_module").my_function.__doc__)'
		     python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
	->	A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

```(3) SQL Scripts```

	->	Allowed editors:
			vi, vim, emacs
	->	All files will be executed on:
			Ubuntu 20.04 LTS
				using:
					MySQL 8.0 (version 8.0.25)
	->	All files should end with a new line
	->	All SQL queries should have a comment just before
	->	All files should start by a comment describing the task
	->	All SQL keywords should be in uppercase:
			SELECT, WHERE…
	->	A README.md file, at the root of the folder of the project, is mandatory
	->	The length of files will be tested using:
			wc

```(4) EXECUTION```

    IN INTERACTIVE MODE:

	$ ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb)
	(hbnb)
	(hbnb) quit
	$


    IN NON-INTERACTIVE MODE:(like the Shell project in C)

	$ echo "help" | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb)
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb)
	$


    ALL TESTS SHOULD ALSO PASS IN NON-INTERACTIVE MODE:

	$ echo "python3 -m unittest discover tests" | bash
