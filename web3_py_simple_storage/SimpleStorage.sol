//SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {

    // This will be initialized to 0!
    uint256 favoriteNumber;

    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People[] public people;
    mapping(string => uint256) public nameToFavoriteNumber;

    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }

    // view and pure are two different types of functions. 
    //Views simply read off the blockchain. 
    //Pure functions only do math and do not save the state on chain.
    function retrieve() public view returns(uint256) {
        return favoriteNumber;
    }

    // You can hold a value in storage or memory
    // In memory data will only be stored during the execution of the function
    // In storage data will persist after the function executes
    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber, _name));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }

}
