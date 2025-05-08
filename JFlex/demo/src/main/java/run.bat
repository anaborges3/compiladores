@echo off
set JFLEX_HOME=C:\Desenvolvimento\jflex-1.9.1

for /D %%d in (src\q*) do (
    java -Xmx128m -jar "%JFLEX_HOME%\lib\jflex-full-1.9.1.jar" %%d\*.flex
    javac %%d\*.java
    java Yylex test.txt
)
pause
