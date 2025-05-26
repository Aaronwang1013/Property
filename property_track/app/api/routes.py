from fastapi import APIRouter
from datetime import date, timedelta
import random


router = APIRouter()


@router.get("/compare")
def compare_performance():
    today = date.today()
    days = [today - timedelta(days=i) for i in reversed(range(30))]
    
    user_returns = [round(random.uniform(-0.05, 0.05), 4) for _ in range(30)]
    market_returns = [round(random.uniform(-0.03, 0.03), 4) for _ in range(30)]

    return {
        "labels": [d.strftime("%Y-%m-%d") for d in days],
        "user_returns": user_returns,
        "market_returns": market_returns
    }