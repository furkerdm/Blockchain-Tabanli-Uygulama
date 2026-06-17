from web3 import Web3
from pymongo import MongoClient
import datetime

# 1. Ayarlar
# Alchemy'den aldığım Sepolia RPC URL
ALCHEMY_URL = "*********"
# MongoDB bağlantı adresim
MONGO_URI = "************"
# Metamask cüzdan adresim
MY_ADDRESS = "**********" 
# Metamask'ten aldığım Private Key
PRIVATE_KEY = "*********" 
# Remix'ten kopyaladığım sözleşme adresi
SOZLESME_ADRESI = "*********"

# 2. Bağlantılar
w3 = Web3(Web3.HTTPProvider(ALCHEMY_URL))
client = MongoClient(MONGO_URI)
db = client["blockchain_projesi"]
koleksiyon = db["islemler"]

# Sözleşme ABI (Fonksiyon haritası)
ABI = [
    {"inputs": [{"internalType": "string", "name": "_veri", "type": "string"}], "name": "veriEkle", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [], "name": "saklananVeri", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}
]
sozlesme = w3.eth.contract(address=SOZLESME_ADRESI, abi=ABI)

# 3. İşlem Fonksiyonu
def blockchain_ve_bulut_kayit(yeni_veri):
    try:
        print("Blockchain'e işlem gönderiliyor...")
        nonce = w3.eth.get_transaction_count(MY_ADDRESS)
        
        # İşlemi oluştur (Sepolia Chain ID: 11155111)
        txn = sozlesme.functions.veriEkle(yeni_veri).build_transaction({
            'chainId': 11155111,
            'gas': 200000,
            'maxFeePerGas': w3.to_wei('50', 'gwei'),
            'maxPriorityFeePerGas': w3.to_wei('1', 'gwei'),
            'nonce': nonce,
        })

        # İmzala ve gönder
        signed_txn = w3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        print(f"✅ İşlem Başarılı! Hash: {tx_hash.hex()}")

        # MongoDB Kaydı
        islem_kaydi = {
            "islem_tarihi": datetime.datetime.now(),
            "eklenen_veri": yeni_veri,
            "islem_hash": tx_hash.hex(),
            "sozlesme_adresi": SOZLESME_ADRESI
        }
        koleksiyon.insert_one(islem_kaydi)
        print("✅ MongoDB'ye başarıyla kaydedildi.")

    except Exception as e:
        print(f"Hata oluştu: {e}")

# Çalıştır
blockchain_ve_bulut_kayit("Proje 5: Alchemy ve MongoDB Entegrasyonu Basarili!")