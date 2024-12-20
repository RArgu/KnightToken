// SPDX-License-Identifier: MIT
// Compatible with OpenZeppelin Contracts ^5.0.0
pragma solidity ^0.8.22;

import {ERC721} from "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import {ERC721Enumerable} from "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import {ERC721URIStorage} from "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Strings.sol"; 

contract KnightToken is ERC721, ERC721Enumerable, ERC721URIStorage, Ownable {
    uint256 private _nextTokenId = 1;
    uint256 public constant maxSupply = 5184;

    constructor(address initialOwner)
        ERC721("KnightToken", "KTK")
        Ownable(initialOwner)
    {}

    function _baseURI() internal pure override returns (string memory) {
        return "https://ipfs.io/ipfs/bafybeigs6mglxbhb37oqppb2wc32tyb4jguctuexsii7ho3ynlwcavnhxm/"; // metadata uri
    }

    function safeMint(address to) public onlyOwner {
        require(_nextTokenId < maxSupply, "Max supply reached");
        uint256 tokenId = _nextTokenId++;
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, string(abi.encodePacked("knight", Strings.toString(tokenId), ".json")));
    }

    function safeMintMulti(address to, uint256 amount) public onlyOwner {
        require(_nextTokenId + amount <= maxSupply, "Exceeds max supply");
        for (uint256 i = 0; i < amount; i++) {
            uint256 tokenId = _nextTokenId++;
            _safeMint(to, tokenId);
            _setTokenURI(tokenId, string(abi.encodePacked("knight", Strings.toString(tokenId), ".json")));
        }
    }

    // The following functions are overrides required by Solidity.

    function _update(address to, uint256 tokenId, address auth)
        internal
        override(ERC721, ERC721Enumerable)
        returns (address)
    {
        return super._update(to, tokenId, auth);
    }

    function _increaseBalance(address account, uint128 value)
        internal
        override(ERC721, ERC721Enumerable)
    {
        super._increaseBalance(account, value);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable, ERC721URIStorage)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}