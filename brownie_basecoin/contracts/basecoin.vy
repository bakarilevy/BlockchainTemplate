# @version ^0.2.0

# Need to keep track of balances
# Retrieve balance
# Transfer from one address to the other
# Give token name

# Billion Tokens
#TOTAL_SUPPLY: constant(uint256) = 10**27 # 10 to the amount of tokens we want + decimals
NAME: constant(String[10]) = 'BaseCoin'
# Ensure your token has the same number of decimals as Ethereum
DECIMALS: constant(uint256) = 18

event Transfer:
    _from: indexed(address)
    _to: indexed(address)
    _value: uint256

event Approve:
    _owner: indexed(address)
    _spender: indexed(address)
    _value: uint256

_balances: HashMap[address, uint256]
# This hashmap is used for working with a DEX
_allowances: HashMap[address, HashMap[address, uint256]]
_totalSupply: uint256
_minted: bool
_minter: address 

# When Contract is deployed sends the whole supply to the contract's sender
@external
def __init__():
    self._minter = msg.sender
    self._minted = False
    self._totalSupply = 5000 * 10**18
    self._balances[msg.sender] = self._totalSupply

@external
def mint(_to: address, tSupply: uint256):
    assert msg.sender == self._minter, 'Only owner of this contract can mint this coin.'
    assert self._minted == False, 'This token has already been minted.'
    self._totalSupply = tSupply * 10 ** DECIMALS
    self._balances[_to] = self._totalSupply
    self._minted = True
    log Transfer(ZERO_ADDRESS, _to, self._totalSupply) # Tracking this event

@external
@view
def name() -> String[10]:
    return NAME

@external
@view
def totalSupply() -> uint256:
    return self._totalSupply / 10 ** 18

@external
@view
def balanceOf(_address:address) -> uint256:
    return self._balances[_address] / 10 ** 18

# Allowance allows one user to move funds on behalf of the other one
@external
@view
def allowance(_owner: address, _spender: address) -> uint256:
    return self._allowances[_owner][_spender]

@external
@view
def decimals() -> uint256:
    return DECIMALS

@internal
def _transfer(_from: address, _to: address, _amount: uint256):
    assert self._balances[_from] >= _amount, 'The balance of this account is not enough to proceed with this transaction.'
    assert _from != ZERO_ADDRESS
    assert _to != ZERO_ADDRESS
    self._balances[_from] -= _amount
    self._balances[_to] += _amount
    log Transfer(_from, _to, _amount)

@internal
def _approve(_owner: address, _spender: address, _amount: uint256):
    assert _owner != ZERO_ADDRESS
    assert _spender != ZERO_ADDRESS
    self._allowances[_owner][_spender] = _amount
    log Approve(_owner, _spender, _amount)

@external
def transfer(_to:address, _amount: uint256) -> bool:
    self._transfer(msg.sender, _to, _amount)
    return True

@external
def approve(_spender:address, _amount:uint256) -> bool:
    self._approve(msg.sender, _spender, _amount)
    return True

@external
def increaseAllowance(_spender: address, _amount_increased: uint256) -> bool:
    self._approve(msg.sender, _spender, self._allowances[msg.sender][_spender] + _amount_increased)
    return True

@external
def decreaseAllowance(_spender: address, _amount_decreased: uint256) -> bool:
    assert self._allowances[msg.sender][_spender] >= _amount_decreased, 'Negative allowance is not allowed.'
    self._approve(msg.sender, _spender, self._allowances[msg.sender][_spender] - _amount_decreased)
    return True

@external
def transferFrom(_owner:address, _to: address, _amount:uint256) -> bool:
    assert self._allowances[_owner][msg.sender] >= _amount, 'The allowance is not enough for this operation.'
    assert self._balances[_owner] >= _amount, 'The balance is not enought for this operation.'
    self._balances[_owner] -= _amount
    self._balances[_to] += _amount
    self._allowances[_owner][msg.sender] -= _amount
    return True

