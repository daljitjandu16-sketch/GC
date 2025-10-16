from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="GoldRocks Dashboard - Public")

# Signals (change BUY/SELL here if needed)
_latest_signals = {'1m': 'BUY', '15m': 'SELL'}

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    html = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="refresh" content="60">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>GoldRocks Dashboard</title>
        <style>
            body {{ background-color: #101010; color: #fff; font-family: Arial, sans-serif; text-align: center; }}
            .container {{ display: flex; justify-content: center; margin-top: 100px; gap: 50px; }}
            .signal-box {{ width: 200px; height: 200px; display: flex; align-items: center; justify-content: center; border-radius: 20px; font-size: 30px; font-weight: bold; }}
            .buy {{ background-color: #0a8f00; }}
            .sell {{ background-color: #c00; }}
        </style>
    </head>
    <body>
        <h1>GoldRocks Signals</h1>
        <div class="container">
            <div class="signal-box {'buy' if _latest_signals['1m']=='BUY' else 'sell'}">1M: {_latest_signals['1m']}</div>
            <div class="signal-box {'buy' if _latest_signals['15m']=='BUY' else 'sell'}">15M: {_latest_signals['15m']}</div>
        </div>
    </body>
    </html>"""
    return HTMLResponse(content=html)
