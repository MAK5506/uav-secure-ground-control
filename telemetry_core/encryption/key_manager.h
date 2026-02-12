#pragma once
#include <vector>
#include <cstdint>

class KeyManager {
public:
    static std::vector<uint8_t> generateSessionKey();
    static std::vector<uint8_t> generateIV();
};

