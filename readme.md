brownie networks add Ethereum ganache-local host=http://127.0.0.1:7545 chainid=5777
brownie networks add development mainnet-fork cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-mainnet.alchemyapi.io/v2/XOHZ5-TWxneYxciHBUdBQM2PP6APhbGW accounts=10 mnemonic=brownie port=8545  

Smart Contract Lottery

1. Users can enter lottery with ETH based on a USD fee
2. An admin will choose when the lottery is over.
3. The lottery will select a random winner