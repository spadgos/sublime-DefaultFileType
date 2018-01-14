This package is a fork of https://github.com/spadgos/sublime-DefaultFileType. Credit goes to [spadgos][spadgos] for the plugin, I just updated its compatibility for Sublime Text 3.

This package sets the default file type of new files to be either the same as the current file, or a predefined default.

This only affects files which are created with the `Ctrl+N` shortcut (`Cmd+N` on OSX), if you wish to change the hotkey you can modify it in the `Default.sublime-keymap` file.

## Installation ##

### With Package Control ###

If you have the [Package Control][package_control] package installed, you can install DefaultFileType from inside Sublime Text itself. Open the Command Palette and select "Package Control: Install Package", then search for DefaultFileType3 and you're done!

### Without Package Control ###

Go to your Sublime Text 3 Packages directory and clone the repository using the command below:

    git clone https://github.com/diegotf30/sublime-DefaultFileType.git DefaultFileType3

## Configuration ##

Edit the file `default_file_type.sublime-settings` in the Packages directory and you can set these options:

- `default_new_syntax` *(String)* This is the default syntax each new window is set to. Default value is `"Python.sublime-syntax"`. 
  
  __Note:__ The syntax for each supported ST3 language is located in `Packages/DefaultFileType3/Syntaxes` (Most of them are just "$language.sublime-syntax")
- `use_current_syntax` *(Boolean)* Set this to `true` to use the current file's syntax for the new file. If `false`, then the default (above) will always be used. Default value is `false`

Let me know if you have any problems or feature requests by adding an issue here: https://github.com/diegotf30/sublime-DefaultFileType

[package_control]: http://wbond.net/sublime_packages/package_control
[spadgos]: https://github.com/spadgos