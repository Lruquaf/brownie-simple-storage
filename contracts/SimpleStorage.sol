// SPDX-License-Identifier: MIT

pragma solidity 0.6.0;

contract SimpleStorage {
    uint256 favouriteNumber;

    struct People {
        uint256 favouriteNumber;
        string name;
    }

    People[] public people;
    mapping(string => uint256) public nameToFavouriteNumber;

    function store(uint256 fav_number) public {
        favouriteNumber = fav_number;
    }

    function retrieve() public view returns (uint256) {
        return favouriteNumber;
    }

    function addPerson(string memory _name, uint256 favorite_Number) public {
        people.push(People(favorite_Number, _name));
        nameToFavouriteNumber[_name] = favorite_Number;
    }
}
