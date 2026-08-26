# -*- coding: utf-8 -*-
"""抓取輔大資管課程作業語料（系／院／校三級規章）。
逐檔下載並回報 HTTP 狀態與大小，失敗不中斷，最後印出彙總表。
"""
import os
import urllib.request
import urllib.parse

BASE = os.path.dirname(os.path.abspath(__file__))   # 腳本所在目錄
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

IM = "https://www.im.fju.edu.tw/wp-content/uploads/"
IMS = "https://www.im.fju.edu.tw/site/wp-content/uploads/"
EDU = "http://docs.academic.fju.edu.tw/edulaw/"
EDU2 = "https://docsacademic.fju.edu.tw/edulaw/"

# (子資料夾, 存檔名, 來源網址)
MANIFEST = [
    # ── 系級：修業規則（7 個年度版本）──
    ("01-系級", "系修業規則-114學年度入學生.pdf", IM + "2025/09/114資訊管理學系修業規則適用114學年度入學生.pdf"),
    ("01-系級", "系修業規則-113學年度新生.pdf",   IM + "2025/09/113資訊管理學系修業規則適用113學年度新生.pdf"),
    ("01-系級", "系修業規則-112學年度新生.pdf",   IM + "2025/09/112資訊管理學系修業規則適用112學年度新生.pdf"),
    ("01-系級", "系修業規則-111學年度新生.pdf",   IMS + "2022/08/111資訊管理學系修業規則適用111學年度新生.pdf"),
    ("01-系級", "系修業規則-109-110學年度新生.pdf", IMS + "2022/01/109資訊管理學系修業規則適用109學年度新生.pdf"),
    ("01-系級", "系修業規則-108學年度新生.pdf",   IMS + "2019/06/108資訊管理學系修業規則適用108學年度新生.pdf"),
    ("01-系級", "系修業規則-107學年度入學生.pdf", "http://140.136.202.160/site/wp-content/uploads/2018/07/107修業規則-適用107-計概和機測.pdf"),
    # ── 系級：必選修科目表（碩士班，中英對照，含學群）──
    ("01-系級", "必選修科目表-114資管碩-中英對照.pdf", IM + "2025/07/必選修科目表-114資管碩-中英對照.pdf"),
    ("01-系級", "必選修科目表-113資管碩-中英對照.pdf", IM + "2025/07/必選修科目表-113資管碩-中英對照.pdf"),
    ("01-系級", "必選修科目表-112資管碩-中英對照.pdf", IM + "2025/07/必選修科目表-112資管碩-中英對照.pdf"),
    ("01-系級", "必選修科目表-111資管碩-中英對照.pdf", IM + "2025/07/必選修科目表-111資管碩-中英對照.pdf"),
    # ── 系級：碩士班暨碩職班課表 ──
    ("01-系級", "課表-115學年.pdf",        IM + "2026/05/115學年碩士班暨碩職班課表.pdf"),
    ("01-系級", "課表-114學年.pdf",        IM + "2025/05/114學年碩士班課表.pdf"),
    ("01-系級", "課表-113學年第2學期.pdf", IM + "2024/11/113學年第二學期碩士班暨碩職班課表.pdf"),
    ("01-系級", "課表-113學年第1學期.pdf", IM + "2024/10/113學年資管碩士碩職班課表202410改教室.pdf"),
    ("01-系級", "課表-112學年第2學期.pdf", IM + "2024/02/112學年第二學期碩士班暨碩職班課表.pdf"),
    ("01-系級", "課表-112學年第1學期.pdf", IMS + "2023/09/112學年第一學期碩士班暨碩職班課表.pdf"),
    ("01-系級", "課表-111學年第2學期.pdf", IMS + "2023/05/111學年第二學期碩士班暨碩職班課表.pdf"),
    ("01-系級", "課表-111學年第1學期.pdf", IMS + "2022/08/111學年第一學期碩士班暨碩職班課表.pdf"),
    ("01-系級", "課表-110學年第2學期.pdf", IMS + "2022/02/110學年第二學期碩士班暨碩職班課表.pdf"),
    ("01-系級", "課表-110學年第1學期.pdf", IMS + "2021/08/1101學年碩士班暨碩職班課表.pdf"),
    # ── 校級：教務處法規庫 ──
    ("03-校級", "輔仁大學學則.pdf",                    EDU + "輔仁大學學則.pdf"),
    ("03-校級", "博士班碩士班研究生學位考試辦法.pdf",   EDU + "輔仁大學學位考試辦法.pdf"),
    ("03-校級", "各類學位授予辦法.pdf",                EDU2 + "學位授予辦法.pdf"),
    ("03-校級", "學生成績考評及學分核計辦法.pdf",       EDU2 + "學生成績考評及學分核計辦法.pdf"),
    ("03-校級", "學生修讀輔系辦法.pdf",                EDU2 + "學生修讀輔系辦法.pdf"),
    ("03-校級", "校際選課實施辦法.pdf",                EDU + "panselcoureg.pdf"),
    ("03-校級", "學生抵免科目規則.pdf",                EDU2 + "學生抵免科目規則.pdf"),
]


def encode(url):
    """只對路徑做百分號編碼，保留 scheme 與 host。"""
    p = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit(
        (p.scheme, p.netloc, urllib.parse.quote(p.path), p.query, p.fragment)
    )


results = []
for folder, name, url in MANIFEST:
    dest = os.path.join(BASE, folder, name)
    try:
        req = urllib.request.Request(encode(url), headers=UA)
        with urllib.request.urlopen(req, timeout=45) as r:
            data = r.read()
        # 確認真的是 PDF，避免把 404 導向的 HTML 存成 .pdf
        if not data.startswith(b"%PDF"):
            results.append((name, "非PDF", len(data), url))
            continue
        with open(dest, "wb") as f:
            f.write(data)
        results.append((name, "OK", len(data), url))
    except Exception as e:
        results.append((name, "失敗:" + type(e).__name__ + " " + str(e)[:60], 0, url))

print("=" * 90)
for name, status, size, url in results:
    print("%-46s %-28s %8s" % (name, status, size if size else ""))
ok = sum(1 for r in results if r[1] == "OK")
print("=" * 90)
print("成功 %d / 共 %d" % (ok, len(results)))
