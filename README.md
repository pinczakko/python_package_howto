# README

This is just a placeholder

# How to Use

- Use: ``` python2 setup.py sdist``` to build the source distribution

- Use: ```stage.sh``` to "stage/deploy" a symlink to the current development dir in the 
  global python2 site-packages directory and register the package to easy_install "database".

- Use: ```unstage.sh``` to remove the symlink to the current development dir in the 
  global python2 site-packages directory and unregister the package from easy_install "database".

