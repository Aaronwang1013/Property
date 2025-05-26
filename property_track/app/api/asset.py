from fastapi import APIRouter
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


router = APIRouter(prefix="/api/v1/assets", tags=["Assets"])
tz = ZoneInfo("Asia/Taipei")



@router.get("/history")
def get_asset_history():
    base_time = datetime.now(tz)
    return {
        "records": [
            {
                "id": i,
                "timestamp": (base_time - timedelta(days=i)).isoformat(),
                "value": 1000 + i * 20,
            }
            for i in range(30)
        ]
    }


