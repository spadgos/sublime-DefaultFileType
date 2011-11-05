This package sets the default file type of new files to be either the same as the current file, or a predefined default.

This only affects files which are created with the `Ctrl+N` shortcut (`Cmd+N` on OSX).

### Configuration ###

Create a file in your `Packages/User` directory called `default_file_type.sublime-settings` and you can set these options:

- `default_new_file_syntax` *(String)* This is the path, relative to the Sublime base directory to the language file you'd like to load as the default. Default value is `"Packages/Java/Java.tmLanguage"`
- `use_current_file_syntax` *(Boolean)* Set this to `true` to use the current file's syntax for the new file. If `false`, then the default (above) will always be used. Defauult value is `true`

Let me know if you have any problems or feature requests by adding an issue here: https://github.com/spadgos/sublime-DefaultFileType
