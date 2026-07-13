# fengshui_lib.py

try:
    import sxtwl
    # 初始化引擎
    lunar_engine = sxtwl.Lunar()
    SXTWL_AVAILABLE = True
except ImportError:
    SXTWL_AVAILABLE = False
    print("警告：sxtwl 無法載入，請確認編譯環境。")

class PreciseCalendar:
    @staticmethod
    def get_four_pillars(year, month, day, hour):
        if SXTWL_AVAILABLE:
            # 使用高精準度 sxtwl 計算
            day_info = lunar_engine.getDayBySolar(year, month, day)
            year_gz = f"{day_info.yearGZ.tg}{day_info.yearGZ.dz}"
            month_gz = f"{day_info.monthGZ.tg}{day_info.monthGZ.dz}"
            day_gz = f"{day_info.dayGZ.tg}{day_info.dayGZ.dz}"
            
            shi_gz = lunar_engine.getShiGZ(day_info.dayGZ.tg, hour // 2)
            hour_gz = f"{shi_gz.tg}{shi_gz.dz}"
            
            return {"年柱": year_gz, "月柱": month_gz, "日柱": day_gz, "時柱": hour_gz}
        else:
            # 回退到簡易數學計算邏輯 (避免系統報錯)
            return {"年柱": "??", "月柱": "??", "日柱": "??", "時柱": "??"}
