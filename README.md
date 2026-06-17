# ⛓️ Hibrit Blok Zinciri ve Bulut Veritabanı Projesi

Bu proje, Ethereum Sepolia ağı, Alchemy RPC ve MongoDB Atlas kullanılarak yüksek erişilebilirlik prensipleriyle geliştirilmiş merkeziyetsiz bir veri yönetim sistemidir. 

## 🚀 Teknolojiler ve 🏗️ Mimari
Remix IDE üzerinden derlenip Sepolia ağına dağıtılan Solidity tabanlı akıllı sözleşmeler, Web3.py kütüphanesi ve Python kullanılarak yönetilmektedir. 

## ☁️ Bulut Altyapısı (Alchemy & RPC)
Yerel düğümler yerine Alchemy bulut altyapısı tercih edilerek ağa kesintisiz erişim sağlanmış ve işlemler özel anahtarlarla güvenli bir şekilde imzalanmıştır. 

## 💾 Veri Yönetimi (MongoDB Atlas)
Blok zinciri üzerindeki yavaş okuma sürelerini aşmak için, başarılı her işlemin benzersiz hash değeri ve meta bilgileri anlık olarak MongoDB Atlas bulut veritabanına indekslenmektedir. 

## 🛠️ Sorun Giderme ve Optimizasyon
Geliştirme sürecinde karşılaşılan işlem imzalama hataları ve yerel ağ senkronizasyon problemleri, güncel Web3 kütüphanesi metotları entegre edilerek başarıyla çözülmüştür.
