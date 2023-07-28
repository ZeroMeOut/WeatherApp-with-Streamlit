set folder="E:\Projects\apacheStuff\kafka\config\tmp\kafka-logs"
cd /d %folder%
for /F "delims=" %%i in ('dir /b') do (rmdir "%%i" /s/q || del "%%i" /s/q)
set folder2="E:\Projects\apacheStuff\kafka\config\tmp\zookeeper"
cd /d %folder2%
for /F "delims=" %%i in ('dir /b') do (rmdir "%%i" /s/q || del "%%i" /s/q)