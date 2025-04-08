from pypsrp.client import Client

client = Client("IP_DO_WINDOWS", username="USUARIO_WINDOWS", password="SENHA_WINDOWS", ssl=False)

command = r'PowerShell -Command "Get-Service -Name MSSQL$ARCAMASTER | Select-Object Status, Name, DisplayName"'
stdout, stderr, rc = client.execute_cmd(command)

print("Saída:", stdout)
print("Erros:", stderr)
