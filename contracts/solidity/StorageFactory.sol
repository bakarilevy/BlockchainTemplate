//SPDX-License-Identifier: MIT

pragma solidity >= 0.6.0 < 0.9.0;

// Path to other smart contract you want to use
import "./SimpleStorage.sol";

// Solidity inheritance
contract StorageFactory is SimpleStorage {

    // After you have called the below function and you view the contents you will see the address of where
    // the instance of the Simple Storage Contract was deployed to
    SimpleStorage[] public simpleStorageArray;

    function createSimpleStorageContract() public {
        // Creates an instance of the imported contract
        SimpleStorage simpleStorage = new SimpleStorage();
        simpleStorageArray.push(simpleStorage);
    }

    // This allows you to select the index of a created Simple Storage Contract and pass a favorite number to it.
    // In order to interact with a created contract you need both the address as well as the application binary interface
    function sfStore(uint256 _simpleStorageIndex, uint256 _simpleStorageNumber) public {
        SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        simpleStorage.store(_simpleStorageNumber);
    }

    // Since this function only reads state off the blockchain it can be a public view function.
    // It returns a uint256 because it calls the selected contracts retrieve favorite number function.
    function sfGet(uint256 _simpleStorageIndex) public view returns (uint256) {
        SimpleStorage simpleStorage =  SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        return simpleStorage.retrieve();
    }

}

