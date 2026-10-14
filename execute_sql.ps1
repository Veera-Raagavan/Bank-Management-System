# Execute bank.sql in MySQL
$sqlFile = Join-Path $PSScriptRoot "bank.sql"
$sqlContent = Get-Content $sqlFile -Raw

# Execute SQL commands
mysql -u root -e $sqlContent

Write-Host "SQL execution completed. Check for any errors above."

