# app/coingecko_client.py
import requests
from .config import COINGECKO_API_KEY, COINGECKO_BASE_URL

def fetch_markets(
	vs_currency: str = "usd", 
	order: str = "market_cap_desc", 
	per_page: int = 50, 
	page: int = 1, 
	sparkline: bool = False, 
): 
	url = f"{COINGECKO_BASE_URL}/coins/markets"
	headers = {"x-cg-api-key": COINGECKO_API_KEY}
	params = {
		"vs_currency": vs_currency, 
		"order": order, 
		"per_page": per_page, 
		"page": page, 
		"sparkline": str(sparkline).lower(),}

	resp = requests.get(url, headers = headers, params = params, timeout = 10)
	resp.raise_for_status()		# will throw if CoinGecko returns error
	return resp.json()

def fetch_market_chart(
	id: str, 
	vs_currency: str, 
	days: str
):
    url = f"{COINGECKO_BASE_URL}/coins/{id}/market_chart"

    headers = {"x-cg-api-key": COINGECKO_API_KEY}
    
    params = {
        "vs_currency": vs_currency,
        "days": days,
    }

    resp = requests.get(url, params=params, headers=headers, timeout=10)
    resp.raise_for_status()
    return resp.json()
