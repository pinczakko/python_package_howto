# README

This project shows:

1. How to create very simple Python 2 package

2. How to test the package by "staging" it into the system's python site-package

3. How to "unstage the package from the system's python site-package

4. How to install the package into the system's python site-package

5. How to uninstall the package from the system's python site-package

# How to Use

- Use: ``` python2 setup.py sdist``` to build the source distribution

- Use: ```stage.sh``` to "stage/deploy" a symlink to the current development dir in the 
  global python2 site-packages directory and register the package to easy_install "database".

- Use: ```unstage.sh``` to remove the symlink to the current development dir in the 
  global python2 site-packages directory and unregister the package from easy_install "database".

- Use: ```install.sh``` to install the current development dir package to the 
  global python2 site-packages directory and register the package to easy_install "database".

- Use: ```uninstall.sh``` to uninstall the current development dir package from the 
  global python2 site-packages directory and unregister the package from easy_install "database".

- Use: ```run_test.sh``` to test the installation of the package. Look at the output of ```test.py``` in 
  the console to check whether the package installation/staging is working or not.
