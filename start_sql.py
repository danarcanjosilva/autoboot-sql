from pypsrp.client import Client

client = Client("IP_DO_WINDOWS", username="USUARIO_WINDOWS", password="SENHA_WINDOWS", ssl=False)

command = r'PowerShell -Command "Start-Service -Name MSSQL$ARCAMASTER"'
stdout, stderr, rc = client.execute_cmd(command)

print("Saída:", stdout)
print("Erros:", stderr)

