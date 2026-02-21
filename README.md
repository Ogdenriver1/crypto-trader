# 🚀 Crypto & Stock Trading Bot

A simple terminal-based trading program for cryptocurrencies, stocks, and forex markets.

## ✨ Features

- 💰 Buy and sell cryptocurrencies
- 📊 Track your portfolio in real-time
- 📈 View current market prices
- 📜 Transaction history
- 💵 Starting balance: $10,000 (virtual money)

## 🛠️ Installation

### Option 1: Git Clone (Recommended)
```bash
git clone https://github.com/YOUR_USERNAME/crypto-trader.git
cd crypto-trader
pip install -r requirements.txt
```

### Option 2: Download ZIP
1. Click the green "Code" button
2. Select "Download ZIP"
3. Unzip and navigate to the folder
4. Run `pip install -r requirements.txt`

### Option 3: Direct Download
[Download ZIP](https://github.com/YOUR_USERNAME/crypto-trader/archive/refs/heads/main.zip)

## 🚀 Quick Start

### Step 1: Install Python
Make sure you have Python 3.7+ installed:
```bash
python3 --version
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Trading Bot
```bash
python3 trader.py
```

## 📖 Usage

### Commands

- **Buy cryptocurrency:**
  ```
  buy bitcoin 0.5
  buy ethereum 2
  ```

- **Sell cryptocurrency:**
  ```
  sell bitcoin 0.25
  sell ethereum 1
  ```

- **Check your portfolio:**
  ```
  portfolio
  ```

- **View transaction history:**
  ```
  history
  ```

- **Check current price:**
  ```
  price bitcoin
  price ethereum
  ```

- **Exit:**
  ```
  quit
  ```

## 📊 Supported Cryptocurrencies

The bot uses the free CoinGecko API. Popular symbols include:
- `bitcoin` - Bitcoin (BTC)
- `ethereum` - Ethereum (ETH)
- `cardano` - Cardano (ADA)
- `solana` - Solana (SOL)
- `ripple` - Ripple (XRP)
- `dogecoin` - Dogecoin (DOGE)

[Full list of supported coins](https://api.coingecko.com/api/v3/coins/list)

## 🔧 Configuration

### Add Stock Trading (Optional)
To enable stock trading, you'll need an API key from providers like:
- [Alpha Vantage](https://www.alphavantage.co/) (Free tier available)
- [Finnhub](https://finnhub.io/) (Free tier available)
- [IEX Cloud](https://iexcloud.io/) (Free tier available)

Set your API key:
```bash
export TRADING_API_KEY="your-api-key-here"
```

## 📁 File Structure

```
crypto-trader/
├── trader.py           # Main trading bot
├── portfolio.json      # Your portfolio data (auto-generated)
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## ⚠️ Disclaimer

**This is a simulation/practice trading bot using virtual money.**

- Default starting balance: $10,000 (not real money)
- Real trading requires connecting to actual exchanges
- For educational purposes only
- Always do your own research before real trading

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

## 📄 License

MIT License - feel free to use and modify!

## 🆘 Support

Having issues? Open an issue on GitHub or contact the maintainer.

---

**Happy Trading!** 📈💰
