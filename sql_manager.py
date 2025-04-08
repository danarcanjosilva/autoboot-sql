from pypsrp.client import Client
from getpass import getpass

def conectar_winrm(ip, usuario, senha):
    try:
        client = Client(
            ip,
            username=usuario,
            password=senha,
            ssl=False,
            auth='basic',
            cert_validation=False,
            encryption='never'  # Evita erro de criptografia com auth 'basic'
        )
        return client
    except Exception as e:
        print(f"❌ Erro ao conectar via WinRM: {e}")
        return None

def executar_comando(client, comando):
    try:
        output, streams, had_errors = client.execute_ps(comando)
        if had_errors:
            print(f"❗ Erros:\n{streams}")
        return output.strip()
    except Exception as e:
        print(f"❌ Erro ao executar comando: {e}")
        return None

def main():
    print("Gerenciador de Serviços SQL Remoto via WinRM\n")

    ip = input("Digite o IP do Windows remoto: ").strip()
    usuario = input("Digite o nome do usuário do Windows: ").strip()
    senha = getpass("Digite a senha do usuário do Windows: ")

    client = conectar_winrm(ip, usuario, senha)
    if not client:
        return

    print("\n🔍 Buscando instâncias SQL...")
    comando_instancias = "Get-Service | Where-Object { $_.Name -like 'MSSQL$*' } | Select-Object -ExpandProperty Name"
    resultado = executar_comando(client, comando_instancias)

    instancias = resultado.splitlines() if resultado else []

    if not instancias:
        print("⚠️ Nenhuma instância SQL foi encontrada.")
        nome_manual = input("⚠️ Deseja iniciar/parar uma instância manualmente? Digite o nome (ex: MSSQL$NOME): ").strip()
        if not nome_manual:
            return
        instancias = [nome_manual]

    print("\n✅ Instâncias SQL encontradas:")
    for i, inst in enumerate(instancias, 1):
        print(f"{i}. {inst}")

    escolha = input("\nDigite o número da instância desejada (ou Enter para usar a primeira): ").strip()
    if not escolha.isdigit():
        escolha = 1
    else:
        escolha = int(escolha)

    if escolha < 1 or escolha > len(instancias):
        print("❌ Escolha inválida.")
        return

    nome_instancia = instancias[escolha - 1]

    print("\nO que deseja fazer com o serviço SQL?")
    print("1 - Iniciar")
    print("2 - Parar")
    print("3 - Reiniciar")
    opcao = input("Digite o número da opção desejada: ").strip()

    comandos = {
        "1": f"Start-Service -Name '{nome_instancia}'",
        "2": f"Stop-Service -Name '{nome_instancia}'",
        "3": f"Restart-Service -Name '{nome_instancia}' -Force"
    }

    comando_escolhido = comandos.get(opcao)
    if not comando_escolhido:
        print("❌ Opção inválida.")
        return

    print(f"\n📤 Comando: {comando_escolhido}")
    resultado = executar_comando(client, comando_escolhido)
    if resultado:
        print(f"\n✅ Resultado:\n{resultado}")

if __name__ == "__main__":
    main()
