# AutoBoot SQL

Scripts Python para controlar o SQL Server remotamente via PowerShell Remoto (WinRM), de sistemas Linux para Windows.

## Funcionalidades

- ✅ Iniciar o serviço SQL Server
- ⛔ Parar o serviço SQL Server
- 🔎 Verificar o status do serviço

---

## ✅ Requisitos

- Python 3 (em seu sistema Linux)
- Pacote Python `pypsrp`
- Windows com WinRM habilitado
- Serviço SQL Server instalado no Windows (nome padrão: `NOME_DA_INSTANCIA`)
- Rede configurada como **Privada** no Windows

---

## 🔧 Instalação e dependências no Linux

Clone o repositório e instale a dependência:

```bash
git clone https://github.com/danarcanjosilva/autoboot-sql.git
cd autoboot-sql
pip install -r requirements.txt
