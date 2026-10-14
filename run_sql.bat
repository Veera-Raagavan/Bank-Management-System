@echo off
echo Executing bank.sql in MySQL...
mysql -u root -p < "%~dp0bank.sql"
pause


