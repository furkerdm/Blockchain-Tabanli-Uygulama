import solcx
from web3 import Web3

# Solidity derleyicisini kur
solcx.install_solc('0.8.0')

# Sözleşmeyi oku ve derle
with open("sozlesme.sol", "r") as file:
    source_code = file.read()

compiled_sol = solcx.compile_standard({
    "language": "Solidity",
    "sources": {"sozlesme.sol": {"content": source_code}},
    "settings": {"outputSelection": {"*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}}}
}, solc_version="0.8.0")

bytecode = compiled_sol["contracts"]["sozlesme.sol"]["VeriKaydi"]["evm"]["bytecode"]["object"]
abi = compiled_sol["contracts"]["sozlesme.sol"]["VeriKaydi"]["abi"]

# Ganache'a bağlan ve sözleşmeyi dağıt
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
w3.eth.default_account = w3.eth.accounts[0]

VeriKaydi = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = VeriKaydi.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Sözleşme başarıyla dağıtıldı! Adres: {tx_receipt.contractAddress}")