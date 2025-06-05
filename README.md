
# Refac 
Simple tool for Python refactoring. \
Supports:
- [x] Module renaming
- [x] Moving functions
- [x] Moving classes
- [x] Correcting imports after all the refactoring

---

## Installation 
```{bash} 
git clone git@github.com:Makariy/pyrefac.git 
cd pyrefac 
python3 -m pip install rope  
```

And add refac to you path 
```{bash}
# For example: 
echo "export PATH=\$PATH:$(pwd)" >> ~/.zshrc
```

## Usage
Go to the project root for refactoring
```{bash}
cd /project/path 
```

You can rename a module
```{bash}
# Rename module in a project
refac rename-module <old-filename> <new-filename>
```

Or move global function/class/variable from one file to another
```{bash}
# Move function from one file to another 
refac move-symbol <source-filename> <symbol-name> <dest-filename>
```

#### Note: all the imports are corrected after refactoring!

### Autocompletition
You can install autocompletition for the refactoring such as the action to perform 
(move-symbol, rename-module, ...) and the positional arguments such as the source/dest filenames.
```{bash}
python3 -m pip install argcomplete
activate-global-python-argcomplete
echo '
eval "$(register-python-argcomplete refac)"
autoload -U bashcompinit
bashcompinit
' >> ~/.zshrc
```
And restart your shell

