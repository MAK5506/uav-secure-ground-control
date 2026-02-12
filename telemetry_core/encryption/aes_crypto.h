#pragma once
#include <string>
#include <vector>

class AESCrypto {
public:
    static std::vector<uint8_t> encrypt(
        const std::vector<uint8_t>& data,
        const std::vector<uint8_t>& key,
        const std::vector<uint8_t>& iv
    );

    static std::vector<uint8_t> decrypt(
        const std::vector<uint8_t>& data,
        const std::vector<uint8_t>& key,
        const std::vector<uint8_t>& iv
    );
};

