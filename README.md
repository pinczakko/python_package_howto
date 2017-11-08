# README

This is just a placeholder

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

