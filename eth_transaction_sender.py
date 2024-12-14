
from web3 import Web3

# Настройка соединения с сетью
infura_url = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'  # Замените на ваш URL Infura
web3 = Web3(Web3.HTTPProvider(infura_url))

# Проверка соединения
if not web3.isConnected():
    print("Ошибка подключения к сети")
    exit()

# Параметры транзакции
private_key = "YOUR_PRIVATE_KEY"  # Замените на ваш приватный ключ
sender_address = "YOUR_WALLET_ADDRESS"  # Замените на ваш адрес
receiver_address = "RECEIVER_WALLET_ADDRESS"  # Замените на адрес получателя
value_in_ether = 0.01  # Сумма перевода в ETH

# Создание и отправка транзакции
nonce = web3.eth.getTransactionCount(sender_address)
tx = {
    'nonce': nonce,
    'to': receiver_address,
    'value': web3.toWei(value_in_ether, 'ether'),
    'gas': 21000,
    'gasPrice': web3.toWei('50', 'gwei'),
}

# Подписание и отправка транзакции
signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(f"Транзакция отправлена, хэш: {web3.toHex(tx_hash)}")
