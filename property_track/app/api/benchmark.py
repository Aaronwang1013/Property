from fastapi import APIRouter
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

router = APIRouter(prefix="/api/v1/benchmark", tags=["Benchmark"])
tz = ZoneInfo("Asia/Taipei")


@router.get("/market")
def get_mock_market_data():
    base_time = datetime.now(tz)

    return {
        "benchmark": "TWII",
        "data": [
            {
                "timestamp": (base_time - timedelta(days=i)).isoformat(),
                "value": 15000 + i * 25,
            }
            for i in range(30)
        ],
    }
