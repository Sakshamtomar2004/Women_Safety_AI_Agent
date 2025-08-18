# save as main.py
from fastapi import FastAPI, Request
import uvicorn
from datetime import datetime

app = FastAPI()

@app.post("/incident")
async def incident(request: Request):
    data = await request.json()
    print("🚨 Incident received:", data)
    return {"status": "ok", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
