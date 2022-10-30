import psutil as ps
import win32gui
import win32process
import playsound


f = open('pid.txt', 'r')

text = f.read()
if text.isnumeric():
    PID = int(text)
    action = 'resume'
else:
    window = win32gui.GetForegroundWindow()
    PID = win32process.GetWindowThreadProcessId(window)[-1]
    action = 'pause'
f.close()

f = open('pid.txt', 'w')
if action == 'pause':
    f.write(str(PID))
f.close()


if ps.pid_exists(PID):
    p = ps.Process(PID)
    
    if action == 'pause':
        playsound.playsound('PauseProgram.wav')
        p.suspend()
    else:
        p.resume()
        playsound.playsound('ResumeProgram.wav')
