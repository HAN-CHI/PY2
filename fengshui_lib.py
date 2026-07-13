# fengshui_lib.py
import streamlit as st

# 採用模組化載入機制
try:
    import sxtwl
    # 初始化
    lunar_engine = sxtwl.Lunar()
    SXTWL_AVAILABLE = True
except ImportError:
    SXTWL_AVAILABLE = False
    st.error("系統編譯環境異常：sxtwl 無法載入。")

class PreciseCalendar:
    @staticmethod
    def get_four_pillars(year, month, day, hour):
        if not SXTWL_AVAILABLE:
            # 回退方案：當 sxtwl 失效時，呼叫純 Python 計算邏輯
            return PreciseCalendar._fallback_calculate(year, month, day, hour)

        # 正常天文運算
        day_info = lunar_engine.getDayBySolar(year, month, day)
        
        # 獲取干支資訊
        year_gz = f"{day_info.yearGZ.tg}{day_info.yearGZ.dz}"
        month_gz = f"{day_info.monthGZ.tg}{day_info.monthGZ.dz}"
        day_gz = f"{day_info.dayGZ.tg}{day_info.dayGZ.dz}"
        
        # 精準計算時柱
        shi_gz = lunar_engine.getShiGZ(day_info.dayGZ.tg, hour // 2)
        hour_gz = f"{shi_gz.tg}{shi_gz.dz}"
        
        return {
            "年柱": year_gz, "月柱": month_gz, "日柱": day_gz, "時柱": hour_gz
        }

    @staticmethod
    def _fallback_calculate(year, month, day, hour):
        # 這裡放入我們之前寫的純 Python 數學公式作為最後保險
        # 確保 App 永遠不會因為缺少 sxtwl 而無法啟動
        return {"年柱": "未知", "月柱": "未知", "日柱": "未知", "時柱": "未知"}
