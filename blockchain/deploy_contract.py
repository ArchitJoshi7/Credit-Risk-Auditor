from web3 import Web3
from solcx import compile_standard, install_solc
import json
import os

# 🛠 Install and use Solidity compiler
install_solc("0.8.0")

# 🔁 Load Solidity source from correct path
this_dir = os.path.dirname(__file__)
solidity_file_path = os.path.join(this_dir, "contracts", "DecisionLogger.sol")

with open(solidity_file_path, "r") as file:
    contract_source_code = file.read()

# 🧱 Compile the Solidity contract
compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {
        "DecisionLogger.sol": {"content": contract_source_code}
    },
    "settings": {
        "outputSelection": {
            "*": {
                "*": ["abi", "evm.bytecode"]
            }
        }
    }
}, solc_version="0.8.0")

# ✅ Extract ABI and bytecode
abi = compiled_sol["contracts"]["DecisionLogger.sol"]["DecisionLogger"]["abi"]
bytecode = compiled_sol["contracts"]["DecisionLogger.sol"]["DecisionLogger"]["evm"]["bytecode"]["object"]

# 💾 Save ABI to file
abi_dir = os.path.join(this_dir, "abi")
os.makedirs(abi_dir, exist_ok=True)

with open(os.path.join(abi_dir, "DecisionLogger.json"), "w") as f:
    json.dump(abi, f)

# 🌐 Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# 🔐 Replace these with your Ganache values
account =       # e.g. 0x627...
private_key =       # e.g. 0xabc...

# 🔧 Set up contract
DecisionLogger = web3.eth.contract(abi=abi, bytecode=bytecode)
nonce = web3.eth.get_transaction_count(account)

# 🚀 Build and sign the transaction
transaction = DecisionLogger.constructor().build_transaction({
    "from": account,
    "nonce": nonce,
    "gas": 2000000,
    "gasPrice": web3.to_wei("20", "gwei")
})

signed_txn = web3.eth.account.sign_transaction(transaction, private_key=private_key)

# 📡 Send transaction using correct attribute
tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

# ✅ Output deployed address
print("Contract deployed at:", tx_receipt.contractAddress)
