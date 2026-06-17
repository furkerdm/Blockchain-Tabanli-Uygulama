// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract VeriKaydi {
    string public saklananVeri;
    
    function veriEkle(string memory _veri) public {
        saklananVeri = _veri;
    }
}