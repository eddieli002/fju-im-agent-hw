# HW6｜指定閱讀池

**十八篇，每組必挑 1 篇、最多 2 篇，先選先得、不重複。** **小組討論後，11/25（W11）上課前填進 HW6 登記試算表（連結在 TronClass 公告）；填之前先看別組填了什麼。**

> **這份清單只給連結，不附 PDF 檔。** 各篇的授權狀況不同，課程無法統一散布，
> 請自行從下面的連結取得。若某一篇你點進去要付費，看該篇的取得方式，
> 或改由**校內網路／圖書館代理**連線。取不到就告訴我，不要卡在那裡。

> **01–10 與 11–18 的差別**：01–10 多數是頂尖研討會論文；11–18 是這學期新增的**學術期刊**論文，
> 其中不少來自軟體工程與醫療領域。你們的題目是審核，**從別的領域類比過來**正是 3-3 與繳交物二要練的能力。

---

## 一、先看這個：頁數不等於工作量

| 篇 | PDF 總頁 | **正文頁** | 備註 |
|---|---:|---:|---|
| 07 Why Do MAS Fail? | 47 | **9** | 後面是參考文獻與附錄 |
| 08 Cut the Crap | 37 | **10** | 同上 |
| 12 CANDOR | 25 | **約 13** | 指定閱讀範圍，見該篇 |
| 13 Self-collaboration | 38 | **約 10** | 指定閱讀範圍，見該篇 |
| 14 CIR3 | 24 | **11** | 結論之後是附錄 |
| 16 AdaCoder | 20 | **約 8** | 指定閱讀範圍，見該篇 |

**下表的「正文頁」或「閱讀範圍」才是你要讀的量。** 期刊論文比研討會論文長，
所以 11–18 有幾篇直接告訴你讀哪幾節。

---

## 二、清單

### 01　MARCH: Multi-Agent Reinforced Check for Hallucination

**正文 10 頁｜ACL 2026｜三個角色怎麼真正分開**

Li, Z., Zhang, Y., Cheng, P., Song, J., Zhou, M., Li, H., Hu, S., Qin, Y., Zhao, E., Jiang, X., & Jiang, G. (2026). ACL 2026, Long Papers, 39389–39415.

- 論文（免費全文）https://aclanthology.org/2026.acl-long.1828/
- 程式碼 https://github.com/Qwen-Applications/MARCH

**在講什麼**：三個角色——作答、把答案拆成可查核的小命題、查核。
查核那個**被刻意遮蔽看不到作答者的原文**，只能靠證據自己重新判斷。

> ⚠ **這篇有一節在講強化學習訓練，那一節不必讀。**
> 只要讀懂 Solver–Proposer–Checker 怎麼分工、為什麼要讓查核者看不到原文（information asymmetry）。
>
> ⚠ **3-3 請注意**：這篇的消融實驗做在訓練獎勵上，**沒有直接拿掉「查核者看不到原文」這個設計**。
> 指出這一點本身就是 3-3 的答案——再說說看，你們要怎麼自己驗證「盲審」到底有沒有用。


---

### 02　ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate

**正文 11 頁｜ICLR 2024｜多個評審怎麼分工**

Chan, C.-M., Chen, W., Su, Y., Yu, J., Xue, W., Zhang, S., Fu, J., & Liu, Z. (2024). ICLR 2024.

- 論文（免費全文）https://arxiv.org/abs/2308.07201
- 程式碼 https://github.com/chanchimin/ChatEval

**在講什麼**：把單一個評分者換成一組有不同人設的評審團，討論後才給評價。
論文比較了不同的角色設定與溝通策略。

---

### 03　Towards Detecting LLMs Hallucination via Markov Chain-based Multi-agent Debate Framework

**正文 8 頁｜IEEE ICASSP 2025｜查核方怎麼自己去找證據**

Sun, X., Li, J., Zhong, Y., Zhao, D., & Yan, R. (2025). IEEE ICASSP 2025.

- 預印本（免費全文）https://arxiv.org/abs/2406.03075
- 正式版在 IEEE Xplore，需訂閱；**預印本內容足夠，不必特地去抓正式版**
- 程式碼：作者未公開

**在講什麼**：先抓出待查的主張、**由主張自己產生查詢去找證據**、再多方驗證。
它的有限狀態機寫法值得看——把「同意／不同意／證據不足／升級」寫成明確的狀態轉移，
而不是靠提示詞說「請討論到有共識」。

---

### 04　A Dynamic LLM-Powered Agent Network for Task-Oriented Agent Collaboration（DyLAN）

**正文 11 頁｜COLM 2024｜誰決定下一個誰上場**

Liu, Z., Zhang, Y., Li, P., Liu, Y., & Yang, D. (2024). COLM 2024.

- 論文（免費全文）https://arxiv.org/abs/2310.02170
- 程式碼 https://github.com/SALT-NLP/DyLAN

**在講什麼**：不要把「誰跟誰講話」寫死。先選出團隊，再依當前任務動態決定通訊結構。

---

### 05　OxyGent: Making Multi-Agent Systems Modular, Observable, and Evolvable via Oxy Abstraction

**正文 8 頁｜ACL 2026 System Demonstrations｜共享狀態要有欄位邊界**

Hu, J., Li, T., Yu, L., & Han, A. (2026). ACL 2026, System Demonstrations, 586–596.

- 論文（免費全文）https://aclanthology.org/2026.acl-demo.58/
- 程式碼 https://github.com/jd-opensource/OxyGent

**在講什麼**：代理、工具、模型都當成可組合的節點，執行圖在跑的時候才長出來，
並提供 session／group 層級的共享資料。

---

### 06　ReConcile: Round-Table Conference Improves Reasoning via Consensus among Diverse LLMs

**正文 10 頁｜ACL 2024｜什麼時候該停、什麼時候該繼續**

Chen, J. C.-Y., Saha, S., & Bansal, M. (2024). ACL 2024.

- 論文（免費全文）https://aclanthology.org/2024.acl-long.381/ 或 https://arxiv.org/abs/2309.13007
- 程式碼 https://github.com/dinobby/ReConcile

**在講什麼**：不同模型各自作答並**附上信心值**，多輪圓桌討論後以信心加權投票取得共識。
重點不是投票本身，是它把「同意」變成一個有數值、可以被檢查的東西。

---

### 07　Why Do Multi-Agent LLM Systems Fail?

**正文 9 頁（PDF 47 頁）｜NeurIPS 2025 Datasets & Benchmarks｜要量什麼才叫驗收**

Cemri, M., Pan, M. Z., Yang, S., Agrawal, L. A., Chopra, B., Tiwari, R., Keutzer, K., Parameswaran, A., Klein, D., Ramchandran, K., Zaharia, M., Gonzalez, J. E., & Stoica, I. (2025). NeurIPS 2025, D&B Track.

- 論文（免費全文）https://arxiv.org/abs/2503.13657
- 失敗分類法與資料 https://github.com/multi-agent-systems-failure-taxonomy/MAST

**在講什麼**：從真實的執行軌跡歸納出 **14 種失敗模式**，分成系統設計、代理間錯位、
驗證與終止三大類。它提醒你：不能只報最終正確率。

> ⚠ **PDF 47 頁，但正文只到第 9 頁**，後面是參考文獻與附錄。

---

### 08　Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems

**正文 10 頁（PDF 37 頁）｜ICLR 2025｜代理一多，token 就爆**

Zhang, G., Yue, Y., Li, Z., Yun, S., Wan, G., Wang, K., Cheng, D., Yu, J., & Chen, T. (2025). ICLR 2025.

- 預印本（免費全文）https://arxiv.org/abs/2410.02506
- ICLR 定稿 https://proceedings.iclr.cc/paper_files/paper/2025/hash/bbc461518c59a2a8d64e70e2c38c4a0e-Abstract-Conference.html

**在講什麼**：多代理最貴的不是推理，是代理之間的廢話。把冗餘訊息剪掉之後，
同樣的表現從 43 美元降到 5.6 美元。

> ⚠ 兩點：**PDF 37 頁，正文只到第 10 頁**。另外，
> **系統名稱叫 AgentPrune，但標題裡沒有這個字**——搜尋或找程式碼時要用 AgentPrune。

---

### 09　ALARA for Agents: Least-Privilege Context Engineering Through Portable Composable Multi-Agent Teams

**正文 7 頁｜arXiv 預印本｜每個代理該拿到多少東西**

Agostino, C. J., & D'Souza, N. (2026). arXiv:2603.20380

- 論文（免費全文）https://arxiv.org/abs/2603.20380
- 實作 https://github.com/NPC-Worldwide/npcsh

**在講什麼**：每個子代理只拿到完成自己角色所需的**最少**上下文與工具。

> ⚠ 這篇是**預印本，尚未確認被任何研討會或期刊接受**。可以報，
> 但報告時要說明這一點——「這是預印本」本身就是文獻判讀的一部分。

---

### 10　Agent-to-Agent (A2A) Protocol Integrated Digital Twin System with AgentIQ

**正文 ≤9 頁｜ACM Multimedia 2025｜代理可以是獨立部署的服務**

Gholizadeh HamlAbadi, K., Vahdati, M., Laamarti, F., & El Saddik, A. (2025).
ACM MM 2025 (Brave New Ideas). DOI 10.1145/3746027.3758176

- 論文 https://dl.acm.org/doi/10.1145/3746027.3758176
- **⚠ 需訂閱。請由校內網路或圖書館代理連線**，校外直接點會被擋

**在講什麼**：把姿態辨識、語音、生理訊號等專門代理透過 A2A 協定串接，
每個代理是**可以獨立部署的端點**，用訊息互通而不是在同一支程式裡互相呼叫函式。

> ⚠ **這篇的內容 W14（12-16）才上課**，比你們報告的日期晚。
> 選它等於提前自學，但只有 9 頁。想把期末做成分散式部署的組可以考慮。

---

### 11　Tool-MAD: A Multi-Agent Debate Framework for Fact Verification With Diverse Tool Augmentation and Adaptive Retrieval

**正文 12 頁｜IEEE Access 2026（期刊）｜查核者的證據要從哪裡來**

Jeong, S., Choi, Y., Kim, J., & Jang, B. (2026). *IEEE Access*, 14, 113608–113622. https://doi.org/10.1109/ACCESS.2026.3716053

- 論文（期刊開放取用，免費全文）https://doi.org/10.1109/ACCESS.2026.3716053
- 預印本 https://arxiv.org/abs/2601.04742

**在講什麼**：兩個辯手各拿**不同的查證工具**——一個查靜態知識庫、一個即時上網搜尋——
互相反駁；法官不參加辯論，只在兩邊談不攏時才看完整紀錄做裁決。

**消融值得看**：兩個辯手都不給工具、給同一種工具、給不同工具，三種配置比出來的差距
（Table 6）。想想看：你們的執行代理與查核代理，**查的是不是同一份資料**？

---

### 12　Hallucination to Consensus: Multi-Agent LLMs for End-to-End JUnit Test Generation（CANDOR）

**閱讀範圍約 13 頁｜ACM TOSEM 2026（期刊）｜多位評審之後，誰來拍板**

Xu, Q., Wang, G., Briand, L., & Liu, K. (2026). *ACM Transactions on Software Engineering and Methodology*. https://doi.org/10.1145/3803418

- 預印本（免費全文）https://arxiv.org/abs/2506.02943
- 期刊版 https://doi.org/10.1145/3803418（需校內網路）
- 程式碼 https://github.com/qiqiguana/candor

**在講什麼**：自動產生軟體測試。多位「評審」各自判斷預期結果對不對，
再由一位「彙整者」綜合大家的理由做最後決定——它拿這個做法跟**直接多數決**比。

> ⚠ **閱讀範圍**：第 1 節（引言）、第 3 節（方法，有完整角色圖）、第 5.3 節（消融）、第 6.1 節。
> 第 4 節的實驗設定與軟體測試指標（coverage、mutation score）**看懂「越高越好」即可，不必深究**。

---

### 13　Self-Collaboration Code Generation via ChatGPT

**閱讀範圍約 10 頁｜ACM TOSEM 2024（期刊）｜一個做、一個查，到底有沒有用**

Dong, Y., Jiang, X., Jin, Z., & Li, G. (2024). *ACM Transactions on Software Engineering and Methodology*, 33(7), Article 189. https://doi.org/10.1145/3672459

- 預印本（免費全文）https://arxiv.org/abs/2304.07590
- 程式碼 https://github.com/YihongDong/Self-collaboration-Code-Generation

**在講什麼**：分析師 → 程式員 ⇄ 測試員，三個角色合作寫程式。
**三個角色其實是同一個 ChatGPT，只是給了不同的角色指令。**

> ⚠ **閱讀範圍**：第 1–3 節、第 4.3 節（RQ2，角色消融）、第 6 節。
>
> 💡 **對繳交物四特別有用**：作業說明的排除條款是「只有人設文字不同、能力完全一樣的模型呼叫不算代理」。
> 這篇的三個角色算不算？附錄的 MBPP 結果裡，三個角色全上反而比只加測試員差——為什麼？

---

### 14　Coordinated LLM Multi-Agent Systems for Collaborative Question-Answer Generation（CIR3）

**正文 11 頁｜Knowledge-Based Systems 2025（期刊）｜太快達成共識也是一種失敗**

Saadaoui, S., & Alonso, E. (2025). *Knowledge-Based Systems*, 330(Part B), 114627. https://doi.org/10.1016/j.knosys.2025.114627

- 論文（期刊開放取用，免費全文）https://doi.org/10.1016/j.knosys.2025.114627
- 程式碼 https://github.com/anonym-nlp-ai/cirrr

**在講什麼**：一群寫手代理分頭產出內容，另有一位專門**唱反調**的代理不斷否決、逼大家修改。
拿掉唱反調的代理之後，系統變得**太快收斂**——品質掉得比拿掉任何其他設計都多。

**對你們的意義**：查核代理第一輪就同意執行代理，是好事還是壞事？

---

### 15　Enhancing Diagnostic Capability with Multi-Agents Conversational Large Language Models（MAC）

**正文 11 頁｜npj Digital Medicine 2025（期刊）｜主審有沒有用？代理越多越好嗎？**

Chen, X., Yi, H., You, M., Liu, W., Wang, L., Li, H., Zhang, X., Guo, Y., Fan, L., Chen, G., Lao, Q., Fu, W., Li, K., & Li, J. (2025). *npj Digital Medicine*, 8, 159. https://doi.org/10.1038/s41746-025-01550-0

- 論文（期刊開放取用，免費全文）https://doi.org/10.1038/s41746-025-01550-0

**在講什麼**：罕見疾病會診。數位醫師代理互相討論，一位主審負責質疑、推動共識、
決定何時結束（達成共識或滿 13 輪）。

**消融值得看**：拿掉主審掉多少？醫師代理從 2 個加到 5 個，正確率怎麼變？
另外，論文試過**替醫師代理指定不同專科——結果沒有顯著改善**。這對繳交物四有什麼啟示？

> 正文的數字有一處與表格不一致（2 個代理：正文寫 31.31%，表寫 31.13%），以表格為準。

---

### 16　AdaCoder: An Adaptive Planning and Multi-Agent Framework for Function-Level Code Generation

**閱讀範圍約 8 頁｜IEEE TSE 2026（期刊）｜先便宜地做，失敗了才升級**

Zhu, Y., Liu, C., He, X., Ren, X., Liu, Z., Pan, R., & Zhang, H. (2026). *IEEE Transactions on Software Engineering*, 52(2), 631–650. https://doi.org/10.1109/TSE.2025.3642621

- 預印本（免費全文）https://arxiv.org/abs/2504.04220
- 期刊版 https://doi.org/10.1109/TSE.2025.3642621（需校內網路）
- 程式碼 https://github.com/YXingo/AdaCoder

**在講什麼**：先讓一個代理直接寫；測試沒過，才啟動除錯與規劃代理。
大部分題目不需要全套流程，所以成本只有其他多代理方法的一小部分。

> ⚠ **閱讀範圍**：引言（Introduction）、方法（Methodology）、代理消融（Ablation Study of AdaCoder’s Agents）三節。
> 前導的實證研究（Empirical Study）可以跳過。**消融表在期刊版是 Table XII，預印本是 Table XI。**
>
> 💡 **對繳交物四特別有用**：論文裡的「Code Evaluator」是一支腳本、「Debug Specialist」是規則。
> 論文稱它們為代理——照課堂的四項判準，它們算嗎？

---

### 17　TDAG: A Multi-Agent Framework Based on Dynamic Task Decomposition and Agent Generation

**正文 10 頁｜Neural Networks 2025（期刊）｜子代理要事先設計好，還是當場生出來**

Wang, Y., Wu, Z., Yao, J., & Su, J. (2025). *Neural Networks*, 185, 107200. https://doi.org/10.1016/j.neunet.2025.107200

- 預印本（免費全文）https://arxiv.org/abs/2402.10178

**在講什麼**：主代理把任務拆成子任務，**每個子任務當場生成一個專屬子代理**，而不是從固定名單裡挑。

> 審核流程通常是固定的。選這篇的組，繳交物二很可能是「不採用」——
> 那是允許的，但要說得出**我們的流程為什麼不需要動態生成**。

---

### 18　Orchestrator Multi-Agent Clinical Decision Support System for Secondary Headache Diagnosis in Primary Care

**正文 9 頁｜JAMIA 2026（期刊）｜一條一條查，交給不同的專科代理**

Wu, X., Zhang, H., Garduno-Rapp, N. E., Rousseau, J. F., Thakkallapally, M., Ji, Y., Visweswaran, S., Peng, Y., & Wang, Y. (2026). *Journal of the American Medical Informatics Association*, 33(10), 1910–1920. https://doi.org/10.1093/jamia/ocag111

- 論文（免費全文）https://pmc.ncbi.nlm.nih.gov/articles/PMC13419605/
- 測試案例與結果 https://github.com/PittNAIL/Jamia-Headache-Paper-Gold-Standard-Data-and-Result

**在講什麼**：一個協調代理把病例分派給 7 個專科代理，每個只判斷一項警訊（red flag）。
這個結構跟你們**逐條查核規章**幾乎一樣。

**消融值得看**：Table 3 比較單一模型與多代理、兩種提示寫法、五種模型大小。
**多代理不是每一種組合都比較好**——找出它在什麼條件下反而變差。

---

## 三、自選篇（3–5 篇）

**3–5 篇，其中 1 篇精讀**，其餘寫回寫表（詳見作業說明第二、三節）。
沒有限制來源，但**每一篇都要說得出它跟你們系統的關係**。

挑一篇有名的卻講不出關聯，分數會比挑一篇冷門但真的解決你問題的低。

> **可以沿用 11/11 提案表 §3 的候選三篇。** 自選篇可以和別組重複；全部自選篇請在 11/25 前填進登記試算表的「自選篇」工作表，並標出精讀的那一篇。
>
> 挑到 **01 MARCH** 的組，建議第 2 篇指定篇挑 **02 ChatEval**（或拿它當自選篇）。
> 兩篇擺在一起正好是「查核者看得到原文 vs 看不到」的對照。
>
> **池子裡沒被選走的篇，也可以拿來當自選篇。**

---

## 四、取不到全文怎麼辦

| 狀況 | 怎麼做 |
|---|---|
| arXiv／ACL Anthology 連結打不開 | 換個網路再試；這兩個站都是免費全文 |
| 第 10 篇被 ACM 擋住 | 用校內網路，或走圖書館的電子資源代理 |
| 第 03 篇的 IEEE 正式版要付費 | **不用抓**，arXiv 預印本的內容足夠 |
| 第 12、13、16、17 篇期刊版要付費 | **讀預印本即可**。這四篇的消融數字已核對與期刊版一致（第 16 篇只差在表號）|
| 還是取不到 | **直接告訴我，不要卡著。** 換一篇或我另外想辦法 |
