
# SQL Manager via WinRM

Gerencie remotamente instâncias do SQL Server em máquinas Windows usando Python via WinRM, diretamente do Linux.

---

## 🚀 Recursos

- Descoberta automática de instâncias MSSQL
- Iniciar, Parar ou Reiniciar instâncias remotamente
- Interface interativa via terminal

---

## 🧰 Requisitos

- Python 3.6+
- Linux Ubuntu/Debian
- Permissão de conexão WinRM no Windows remoto

Instale as dependências com:

```bash
git clone https://github.com/danarcanjosilva/autoboot-sql.git
cd autoboot-sql
pip install -r requirements.txt
```

> `requirements.txt` inclui:
> - pypsrp

---

## 📁 Estrutura do Projeto

```bash
sql-manager/
├── sql_manager.py          # Script interativo principal
├── requirements.txt        # Dependências Python
└── README.md
```

---

## 🚧 Configuração no Windows remoto

No PowerShell como **Administrador**:

```powershell
winrm quickconfig -q
winrm set winrm/config/service/auth '@{Basic="true"}'
winrm set winrm/config/service '@{AllowUnencrypted="true"}'

# (Opcional) Liberar porta no firewall
netsh advfirewall firewall add rule name="WinRM HTTP" dir=in action=allow protocol=TCP localport=5985

Restart-Service WinRM
```

---

## 📚 Como Usar

### Executar via terminal:

```bash
python3 sql_manager.py
```

---


Desenvolvido por Daniel Arcanjo da Silva


