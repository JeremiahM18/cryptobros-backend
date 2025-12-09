# app/main.py
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from .coingecko_client import fetch_markets, fetch_market_chart

app = FastAPI(title = "CryptoBros Secure Backend")

# Allow Android emulator / device in dev
app.add_middleware(
	CORSMiddleware,
	allow_origins = ["*"],		# tighten later in prod
	allow_credentials = True,
	allow_methods = ["*"],
	allow_headers = ["*"],
)

@app.get("/wakeup")
def wakeup():
    return {"status": "awake"}

@app.get("/market_chart/{id}")
def get_market_chart(id: str,
                     vs_currency: str = "usd",
                     days: str = "1"):
    try:
        data = fetch_market_chart(id, vs_currency, days)
        return data
     except Exception as e:
        print("ERROR FETCHING MARKET CHART:", e)  # <-- ADD THIS
        raise HTTPException(status_code=502, detail="Upstream API error")

@app.get("/markets")
def get_markets(
	vs_currency: str = Query("usd"),
	order: str = Query("market_cap_desc"),
	per_page: int = Query(50, ge = 1, le = 250),
	page: int = Query(1, ge = 1),
	sparkline: bool = Query(False),
):
	try:
		data = fetch_markets(
			vs_currency = vs_currency,
			order = order,
			per_page = per_page,
			page = page,
			sparkline = sparkline,
		)
		return data
	except Exception as e:
		# Keep details out of the response; log in real system
		raise HTTPException(status_code = 502, detail = "Upstream API error")