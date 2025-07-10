// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DecisionLogger {
    struct Log {
        string hash;
        uint timestamp;
    }

    mapping(string => Log) public logs;

    function logHash(string memory id, string memory hashValue, uint timestamp) public {
        logs[id] = Log(hashValue, timestamp);
    }

    function getHash(string memory id) public view returns (string memory, uint) {
        return (logs[id].hash, logs[id].timestamp);
    }
}
