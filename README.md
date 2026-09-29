# 人工智慧代理人　作業資料

輔仁大學資訊管理學系碩士班．2026 秋季

本 repo 提供課程作業所需的語料、起始 notebook、作答本與作業說明。

---

## 開放時程

**整學期的內容列在下表，但檔案是逐週放上來的。** 標示「未開放」的項目在該週課堂上才會出現在這個 repo 裡，現在點了會是 404，這是正常的。

| 週 | 日期 | 開放的檔案 | 狀態 |
|---|---|---|---|
| **W3** | 09-30 | `HW1/`、`hw-corpus/01-系級/` | ✅ **已開放** |
| W5 | 10-14 | `HW2/`、`hw-corpus/02-院級/`、`HW1/HW1-solution.ipynb` | 未開放 |
| W7 | 10-28 | `HW3/`、`HW4/`、`hw-corpus/03-校級/`、`期中提案/` | 未開放 |
| W10 | 11-18 | `HW6/` | 未開放 |
| W11 | 11-25 | `HW5/` | 未開放 |

> 為什麼要這樣做：每一份作業都有「先自己想、再看答案」的設計，
> 幾份作業之間也有先後依賴。提早拿到後面的檔案，對你自己沒有好處。
> **需要的東西一定會在你需要的那一週出現。**

---

## 目錄結構

```
fju-im-agent-hw/
├── HW1/ … HW6/        每份作業一個資料夾（starter、作答本、教師完成版）
├── 期中提案/            W9 期中提案的說明卡、提案表與參考範例
└── hw-corpus/          全課程共用語料，依層級分三層
    ├── 01-系級/  02-院級/  03-校級/     原始 PDF
    ├── text/                          參考解析輸出
    └── SOURCES.md                     每份文件的來源與適用學年度
```

**語料放在最外層、不放進各作業資料夾**，因為 HW1–HW5 共用同一批語料，
而且 notebook 裡的下載指令是整包複製到 `/content/hw-corpus/`，全班路徑一致。

---

## 內容

### 作業

| 路徑 | 說明 | 開放 |
|---|---|:--:|
| `HW1/HW1-starter.ipynb` | HW1 起始 notebook（四個 TODO 程式挖空） | W3 |
| `HW1/HW1-作答本.docx` | **HW1 的文字作答一律寫在這裡**，見下方說明 | W3 |
| `HW1/HW1-solution.ipynb` | HW1 教師完成版，同時是 HW2 要用的檢索器 | W5 |
| `HW2/HW2-starter.ipynb` | HW2 起始 notebook | W5 |
| `HW3/HW3-starter.ipynb` | HW3 起始 notebook（**會用到 Node／npm**） | W7 |
| `HW4/HW4-starter.ipynb` | HW4 起始 notebook | W7 |
| `HW5/HW5-starter.ipynb` | HW5 起始 notebook（**需要 GPU**） | W11 |
| `HW6/HW6-作業說明.md` | HW6 作業說明（文獻報告與架構修訂，**不寫程式**） | W10 |
| `HW6/HW6-指定閱讀清單.md` | HW6 指定閱讀池十篇的書目與取得連結 | W10 |

### 期中提案（W9）

| 路徑 | 說明 | 開放 |
|---|---|:--:|
| `期中提案/六題型說明卡.md` | 期末專題的**六個候選題型**，一組挑一個 | W7 |
| `期中提案/期中提案表.docx` | **W9 要填的提案表**，一組一份 | W7 |
| `期中提案/期中提案表-參考範例.html` | 上表填好的參考範例，示範每一節要寫到多具體 | W7 |

### 語料

| 路徑 | 說明 | 開放 |
|---|---|:--:|
| `hw-corpus/01-系級/` | 資訊管理學系規章（原始 PDF） | W3 |
| `hw-corpus/02-院級/` | 管理學院規定 | W5 |
| `hw-corpus/03-校級/` | 校級法規（原始 PDF） | W7 |
| `hw-corpus/text/` | 參考解析輸出，依層級分三個子資料夾 | 同上 |
| `hw-corpus/SOURCES.md` | 每份文件的來源網址、頁數與適用學年度 | W3 起逐週補 |

---

## 作答本怎麼用（HW1 起適用）

**文字作答寫在 `.docx`，程式寫在 `.ipynb`。**

| 寫在哪 | 內容 |
|---|---|
| `HW1/HW1-作答本.docx` | 全部 16 處文字作答（名詞定義、觀察、失敗歸因、回望⋯⋯） |
| `HW1/HW1-starter.ipynb` | 四個 TODO 程式挖空，以及執行結果 |

繳交兩件：`HW1_學號_姓名.ipynb` 與 `HW1_學號_姓名.docx`。

> 之所以把文字作答搬出 notebook：在 Colab 裡填 markdown 表格，答案只要出現一個
> 直線符號整張表就崩掉，你看不出哪裡壞了，改作業的人也讀不到你寫了什麼。

---

## 在 Colab 開啟

在 Colab 選「GitHub」分頁貼上本 repo 網址，或直接開啟（**未開放的週次連結會是 404**）：

```
https://colab.research.google.com/github/eddieli002/fju-im-agent-hw/blob/main/HW1/HW1-starter.ipynb
https://colab.research.google.com/github/eddieli002/fju-im-agent-hw/blob/main/HW2/HW2-starter.ipynb
https://colab.research.google.com/github/eddieli002/fju-im-agent-hw/blob/main/HW3/HW3-starter.ipynb
https://colab.research.google.com/github/eddieli002/fju-im-agent-hw/blob/main/HW4/HW4-starter.ipynb
https://colab.research.google.com/github/eddieli002/fju-im-agent-hw/blob/main/HW5/HW5-starter.ipynb
```

開啟後請先**複製到雲端硬碟**，否則你的作答不會被保存。

**HW1 需要 GPU**：執行階段 → 變更執行階段類型 → T4 GPU。

**HW3 會用到 Node／npm**（Colab 已內建，不用自己裝）。第一格會花一兩分鐘下載套件，這是正常的。

**HW5 需要 GPU，且要下載一份 15.2 GB 的模型權重**，依網速約 9–15 分鐘，這是正常的。
**盡量一次做完**——Colab 關掉再開，權重要重新下載一次。

**HW6 不需要 Colab**，直接讀 `HW6/HW6-作業說明.md` 即可。

---

## 平台中立

本課程不指定 LLM 供應商。需要呼叫模型的作業會同時偵測
`OPENAI_API_KEY` 與 `GEMINI_API_KEY`，你設哪一把就用哪一把。

**HW1 完全不需要 API 金鑰**，只做檢索，不做生成。
