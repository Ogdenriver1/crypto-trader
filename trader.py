#!/usr/bin/env python3
"""
Crypto & Stock Trading Bot
A simple trading program for cryptocurrencies, stocks, and forex
"""

import os
import json
from datetime import datetime
import requests

class Trader:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('TRADING_API_KEY')
        self.portfolio = self.load_portfolio()
        self.balance = self.portfolio.get('balance', 10000.0)  # Starting balance
        self.cached_prices = {}  # Cache prices until explicitly refreshed
        
    def load_portfolio(self):
        """Load portfolio from file"""
        try:
            with open('portfolio.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {'balance': 10000.0, 'holdings': {}, 'history': []}
    
    def save_portfolio(self):
        """Save portfolio to file"""
        with open('portfolio.json', 'w') as f:
            json.dump(self.portfolio, f, indent=2)
    
    def get_price(self, symbol, asset_type='crypto', refresh=False):
        """Get current price of an asset"""
        symbol_lower = symbol.lower()
        
        # Return cached price unless refresh is requested
        if not refresh and symbol_lower in self.cached_prices:
            return self.cached_prices[symbol_lower]
        
        # Generate new price
        import random
        
        # Base prices with custom fluctuation ($15k-$90k for Bitcoin)
        base_prices = {
            'bitcoin': 52500,  # Will range from $15,000 to $90,000
            'btc': 52500,
            'ethereum': 2800,
            'eth': 2800,
            'dogecoin': 0.08,
            'doge': 0.08,
            'cardano': 0.45,
            'ada': 0.45,
            'solana': 110,
            'sol': 110,
            'ripple': 0.52,
            'xrp': 0.52,
            'litecoin': 85,
            'ltc': 85,
        }
        
        if symbol_lower in base_prices:
            # Bitcoin ranges from $15,000 to $90,000
            if symbol_lower in ['bitcoin', 'btc']:
                price = random.uniform(15000, 90000)
            else:
                # Other cryptos use ±50% fluctuation
                base = base_prices[symbol_lower]
                fluctuation = random.uniform(-0.50, 0.50)
                price = base * (1 + fluctuation)
            
            # Cache the price
            self.cached_prices[symbol_lower] = price
            return price
        
        return None
    
    def buy(self, symbol, amount, asset_type='crypto'):
        """Buy an asset"""
        price = self.get_price(symbol, asset_type)
        if price is None:
            print(f"❌ Unknown crypto: {symbol}")
            print("Available: bitcoin, ethereum, dogecoin, cardano, solana, ripple, litecoin")
            return False
        
        cost = price * amount
        if cost > self.balance:
            print(f"Insufficient funds. Need ${cost:.2f}, have ${self.balance:.2f}")
            return False
        
        # Execute buy
        self.balance -= cost
        self.portfolio['balance'] = self.balance
        
        if symbol not in self.portfolio['holdings']:
            self.portfolio['holdings'][symbol] = 0
        self.portfolio['holdings'][symbol] += amount
        
        # Record transaction
        transaction = {
            'type': 'BUY',
            'symbol': symbol,
            'amount': amount,
            'price': price,
            'cost': cost,
            'timestamp': datetime.now().isoformat()
        }
        self.portfolio['history'].append(transaction)
        self.save_portfolio()
        
        print(f"✅ Bought {amount} {symbol.upper()} @ ${price:.2f} = ${cost:.2f}")
        print(f"💰 New balance: ${self.balance:.2f}")
        return True
    
    def sell(self, symbol, amount, asset_type='crypto'):
        """Sell an asset"""
        if symbol not in self.portfolio['holdings'] or self.portfolio['holdings'][symbol] < amount:
            print(f"Insufficient {symbol.upper()}. Have {self.portfolio['holdings'].get(symbol, 0)}")
            return False
        
        price = self.get_price(symbol, asset_type)
        if not price:
            print("Could not fetch price")
            return False
        
        # Execute sell
        revenue = price * amount
        self.balance += revenue
        self.portfolio['balance'] = self.balance
        self.portfolio['holdings'][symbol] -= amount
        
        # Record transaction
        transaction = {
            'type': 'SELL',
            'symbol': symbol,
            'amount': amount,
            'price': price,
            'revenue': revenue,
            'timestamp': datetime.now().isoformat()
        }
        self.portfolio['history'].append(transaction)
        self.save_portfolio()
        
        print(f"✅ Sold {amount} {symbol.upper()} @ ${price:.2f} = ${revenue:.2f}")
        print(f"💰 New balance: ${self.balance:.2f}")
        return True
    
    def show_portfolio(self):
        """Display current portfolio"""
        print("\n" + "="*50)
        print("📊 YOUR PORTFOLIO")
        print("="*50)
        print(f"💵 Cash Balance: ${self.balance:.2f}")
        print("\n📈 Holdings:")
        
        total_value = self.balance
        for symbol, amount in self.portfolio['holdings'].items():
            if amount > 0:
                price = self.get_price(symbol)
                if price:
                    value = price * amount
                    total_value += value
                    print(f"  {symbol.upper()}: {amount} @ ${price:.2f} = ${value:.2f}")
        
        print(f"\n💎 Total Portfolio Value: ${total_value:.2f}")
        profit = total_value - 10000.0
        print(f"📊 Profit/Loss: ${profit:.2f} ({(profit/10000.0)*100:.2f}%)")
        print("="*50 + "\n")
    
    def show_history(self, limit=10):
        """Show recent transaction history"""
        print("\n" + "="*50)
        print("📜 TRANSACTION HISTORY")
        print("="*50)
        
        history = self.portfolio['history'][-limit:]
        for tx in reversed(history):
            timestamp = tx['timestamp'].split('T')[0]
            if tx['type'] == 'BUY':
                print(f"🟢 {timestamp} | BUY {tx['amount']} {tx['symbol'].upper()} @ ${tx['price']:.2f} = ${tx['cost']:.2f}")
            else:
                print(f"🔴 {timestamp} | SELL {tx['amount']} {tx['symbol'].upper()} @ ${tx['price']:.2f} = ${tx['revenue']:.2f}")
        print("="*50 + "\n")


def main():
    """Main trading interface"""
    print("🚀 Crypto & Stock Trading Bot")
    print("="*50)
    
    trader = Trader()
    
    while True:
        print("\nCommands:")
        print("  buy <symbol> <amount>  - Buy asset (e.g., buy bitcoin 0.5)")
        print("  sell <symbol> <amount> - Sell asset")
        print("  portfolio              - Show your portfolio")
        print("  history               - Show transaction history")
        print("  price <symbol>        - Check current price")
        print("  quit                  - Exit")
        
        command = input("\n> ").strip().lower()
        
        if command == 'quit':
            print("👋 Goodbye!")
            break
        elif command == 'portfolio':
            trader.show_portfolio()
        elif command == 'history':
            trader.show_history()
        elif command.startswith('buy '):
            parts = command.split()
            if len(parts) == 3:
                _, symbol, amount = parts
                trader.buy(symbol, float(amount))
        elif command.startswith('sell '):
            parts = command.split()
            if len(parts) == 3:
                _, symbol, amount = parts
                trader.sell(symbol, float(amount))
        elif command.startswith('price '):
            symbol = command.split()[1]
            price = trader.get_price(symbol, refresh=True)  # Force refresh when checking price
            if price:
                print(f"💵 {symbol.upper()}: ${price:.2f}")
        else:
            print("❌ Unknown command")


if __name__ == '__main__':
    main()
