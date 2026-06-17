# ⛓️ Hibrit Blok Zinciri ve Bulut Veritabanı Entegrasyonu

Bu proje; Ethereum Sepolia test ağı, Alchemy bulut altyapısı ve MongoDB Atlas kullanılarak geliştirilmiş kapsamlı bir hibrit blok zinciri uygulamasıdır. Proje, akıllı sözleşmeler aracılığıyla blok zincirinin güvenliğini sağlarken, işlem verilerini (hash, tarih, meta veriler) hızlı sorgulanabilir ve indekslenebilir bir şekilde bulut veritabanında saklamayı amaçlar.

## 🚀 Teknolojiler ve Mimari

* **Blockchain Ağı:** Ethereum Sepolia TestNet (Akıllı sözleşmeler Solidity ve Remix IDE ile yazılıp dağıtılmıştır).
* **Bulut Altyapısı (RPC):** Alchemy (Uygulamanın yerel bir bilgisayar bağımlılığı olmaksızın ağla 7/24 kesintisiz iletişim kurmasını sağlar).
* **Bulut Veritabanı:** MongoDB Atlas (Blok zinciri üzerindeki işlemlerin hızlı sorgulanabilir bir kopyasını tutar).
* **Köprü Yazılımı:** Python ve Web3.py (Blok zinciri ile veritabanı arasında köprü görevi görerek işlemleri `PRIVATE_KEY` ile imzalar).

## 🛠️ Kurulum ve Bağımlılıklar

Projeyi yerel bilgisayarınıza klonladıktan sonra terminal üzerinden aşağıdaki komutu çalıştırarak Web3 ve PyMongo gibi gerekli tüm bağımlılıkları sisteminize kurmalısınız:

```bash
pip install -r requirements.txt
