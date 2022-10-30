<h2>PauseProgram windows app</h2>
<p>
PauseProgram is a program to pause and resume programs that are resource heavy and will still work in background.

When you make a pause in a game or other resource heavy programs, you can just hit a shortcut key combination to toggle it from paused to resumed.
</p>
<b>Usage:</b>
<p>
Open PauseProgram.exe
Hit a shortcut key combination (default ctrl + "`") with the program to be paused put in foreground.
Windows may think it became unresponsive, but it's just paused.
Hit that shortcut again (no need to focus) and it resumes.
This program can only pause one program at a time. It was tested with windows 10.
</p>
<p>
Warning! There might be a case of not being able to resume programs, thus losing all your unsaved data. As far as I know it's Windows limitation.
</p>
<p>
The program was inspired by "Resource Monitor" which has the same function built-in, but hard to access.
It was coded in Python and compiled with pyinstaller to .exe app. Sohrtcut key detection uses AutoHotKey program and can be modifable with it.
Program uses sounds from pixabay.com