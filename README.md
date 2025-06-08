
# Pyrefac 
Simple tool based on rope for Python refactoring. \
Supports:
- [x] Module renaming
- [x] Moving functions
- [x] Moving classes
- [x] Moving variables
- [x] Correcting imports after all the refactoring

---

## Installation 
```{bash} 
git clone git@github.com:Makariy/pyrefac.git 
```

And add pyrefac to you path 
```{bash}
# For example: 
cd pyrefac 
echo "export PATH=\$PATH:$(pwd)" >> ~/.zshrc
```

## Usage
Go to the project root for refactoring
```{bash}
cd </project/path>
```

Move global function/class/variable from one file to another:
```{bash}
# Move symbol from one file to another 
refac move-symbol <source-filename> <symbol-name> <dest-filename>
```

Rename a module. (Note that the first parameter is the path to that 
file, and the second is the new filename, not the new path)
```{bash}
# Rename module in a project
pyrefac rename-module <path-to-old-file> <new-filename>
```

See the help for more
```{bash}
pyrefac -h 
```

#### Note: all the imports are corrected after refactoring!

### Autocompletition
You can install autocompletition for the refactoring such as the action to perform 
(move-symbol, rename-module, ...) and the positional arguments such as the source/dest filenames.
```{bash}
python3 -m pip install argcomplete
activate-global-python-argcomplete
echo '
eval "$(register-python-argcomplete pyrefac)"
autoload -U bashcompinit
bashcompinit
' >> ~/.zshrc
```
And restart your shell

