from web3 import Web3

# Ganache RPC Server adresini buraya girin (Ganache ekranındaki adresle aynı olmalı)
ganache_url = "http://127.0.0.1:7545" 
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Bağlantıyı kontrol et
if web3.is_connected():
    print("Harika! Ganache ağına başarıyla bağlandık.")
    
    # Ganache'ın bize verdiği ilk hesabın adresini ve bakiyesini çekelim
    ilk_hesap = web3.eth.accounts[0]
    bakiye_wei = web3.eth.get_balance(ilk_hesap)
    bakiye_eth = web3.from_wei(bakiye_wei, 'ether')
    
    print(f"İlk Hesabın Adresi: {ilk_hesap}")
    print(f"Hesap Bakiyesi: {bakiye_eth} ETH")
else:
    print("Bağlantı başarısız. Ganache'ın açık olduğundan ve RPC URL'sinin doğru olduğundan emin olun.")