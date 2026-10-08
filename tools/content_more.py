# Copy for the Security and FAQ pages, English and Traditional Chinese.

SECURITY = {
    "en": dict(
        eyebrow="Security",
        h1="The input is hostile. MARS is built on that assumption.",
        lead="Every email, link, attachment and XDR field MARS handles was written by someone else, often an attacker. These are the controls at each point where that material crosses a boundary.",
        bounds_h="Five boundaries, and what guards each",
        bounds=[
            ("Reading hostile input", "Mail and attachments are parsed and inspected, never run.", [
                "Attachments are analysed statically. Archives are unpacked within fixed limits on depth, entry count, size and compression ratio.",
                "Every hop of a link is checked before MARS connects, and addresses inside your network are refused.",
                "Parsing is bounded: nesting is capped and the scanning steps take time in proportion to the size of the mail.",
                "Sandbox containers run with all capabilities dropped and no way to gain privileges.",
            ]),
            ("What is sent to the AI", "The model sees evidence, marked as evidence.", [
                "Attacker-controlled text is wrapped in a boundary with a fresh random marker on every call. Forged markers inside the text are neutralised.",
                "Internal mailboxes and account names can be replaced with pseudonyms before a prompt leaves, and restored in the reply.",
                "The AI endpoints MARS may contact are set on the host. The web console cannot widen that list.",
                "When a prompt is too large, evidence is dropped whole, so the boundaries and rules stay intact.",
            ]),
            ("What comes back", "An answer is checked before anyone sees it.", [
                "The reply must fit a closed schema. A truncated or malformed reply is rejected.",
                "A conclusion with too little evidence behind it is withheld.",
                "Anything that fails a check stops at \"needs review\", with a reason code.",
                "There is no path that executes a response action without a person approving it.",
                "A change of model or instructions must pass a replay of known cases first.",
            ]),
            ("Console and API", "Signed-in users get what their role allows.", [
                "Permissions are set per role, per module and per action. The read-only role cannot change anything.",
                "API keys are stored as hashes and can be rotated with a grace period.",
                "Sign-in can use LDAP over an encrypted connection, or OpenID Connect.",
                "Hunting queries, whether written by a person or by the AI, are validated against an allowlist before they run.",
                "Every write is recorded in a signed audit log kept in its own database.",
            ]),
            ("Settings and secrets", "Secrets stay out of the browser.", [
                "Provider keys, the session secret and the audit signing key live in a root-owned file on the host and cannot be edited from the console.",
                "Each setting has one source of truth, so a value shown is the value in effect.",
                "Update packages are verified by checksum before they are applied.",
                "Backups run on a schedule, and another is taken before every database migration.",
            ]),
        ],
        limits_e="Known limits",
        limits_h="What MARS does not protect against",
        limits_p="A security product should say where its guarantees end.",
        limits=[
            ("One instance", "MARS runs as a single instance on one host. It is not a high-availability cluster."),
            ("The sandbox is not the last line", "Containers are hardened, but put them on a network segment you can throw away."),
            ("The AI provider is outside", "MARS checks what a provider returns. It cannot promise the provider keeps no record of what it was sent. Choose where the model runs accordingly."),
            ("ARC signatures are not verified", "Authentication results forwarded through an ARC chain are passed to the AI as claims, with that caveat."),
            ("The host is yours", "Patching, disk encryption, network segmentation and off-site backups are the deployer's responsibility."),
            ("Judgement can still be wrong", "The checks catch unsupported answers. They do not make the model right, which is why response actions need a person."),
        ],
        report_h="Reporting a vulnerability",
        report_p="Report a suspected vulnerability in a deployment to that deployment's MARS administrator, not in a public issue.",
    ),
    "zh": dict(
        eyebrow="安全",
        h1="輸入本來就有敵意，MARS 以此為前提設計。",
        lead="MARS 處理的每一封郵件、每個連結、附件和 XDR 欄位，都是別人寫的，而且常常是攻擊者。以下是這些內容每跨過一道邊界時的控制。",
        bounds_h="五道邊界，各自由什麼把關",
        bounds=[
            ("讀取帶敵意的輸入", "郵件和附件只被解析與檢查，不會被執行。", [
                "附件一律靜態分析。壓縮檔在固定的深度、項目數、大小和壓縮比上限內解開。",
                "連結的每一跳在連線前都先檢查，指向內部網路的位址一律拒絕。",
                "解析有上限：巢狀層數有限制，掃描步驟的耗時只隨郵件大小等比例增加。",
                "沙箱容器移除所有 capability，也無法取得額外權限。",
            ]),
            ("送給 AI 的內容", "模型看到的是證據，而且被標成證據。", [
                "攻擊者可控的文字包在邊界裡，每次呼叫都換一個隨機標記；文字中偽造的標記會被中和。",
                "內部信箱和帳號名稱可以在送出前換成化名，回覆時再還原。",
                "MARS 可以連線的 AI 服務位址由主機設定，主控台無法放寬。",
                "prompt 太大時整段略去證據，邊界和規則保持完整。",
            ]),
            ("AI 的回覆", "答案先檢查，才會有人看到。", [
                "回覆必須符合封閉的格式。被截斷或格式不符的回覆不採用。",
                "證據不足的結論不發佈。",
                "沒通過檢查的一律停在「需要複核」，並附上原因代碼。",
                "沒有任何路徑能在無人核准的情況下執行處置。",
                "更換模型或調整指示之前，必須先通過已知案例的重跑。",
            ]),
            ("主控台與 API", "登入的使用者只能做角色允許的事。", [
                "權限依角色、模組和動作設定。唯讀角色無法變更任何東西。",
                "API key 以雜湊儲存，可以輪替並保留寬限期。",
                "登入可使用加密連線的 LDAP，或 OpenID Connect。",
                "搜捕查詢不論是人寫的還是 AI 寫的，執行前都先對照白名單驗證。",
                "每一次寫入都記錄在有簽章的稽核日誌，存在獨立的資料庫。",
            ]),
            ("設定與密鑰", "密鑰不會出現在瀏覽器裡。", [
                "Provider 金鑰、session 密鑰和稽核簽章金鑰放在主機上屬於 root 的檔案，無法從主控台編輯。",
                "每個設定只有一個來源，畫面上看到的值就是實際生效的值。",
                "更新封包在套用前先核對檢查碼。",
                "備份依排程執行，每次資料庫遷移前另外再備一份。",
            ]),
        ],
        limits_e="已知限制",
        limits_h="MARS 不保護的範圍",
        limits_p="資安產品應該說清楚保證到哪裡為止。",
        limits=[
            ("單一實例", "MARS 以單一實例跑在一台主機上，不是高可用叢集。"),
            ("沙箱不是最後一道防線", "容器有硬化，但請放在可以丟棄的網段。"),
            ("AI provider 在外部", "MARS 會檢查 provider 的回覆，但無法保證 provider 不留下送出的內容。請據此決定模型在哪裡跑。"),
            ("不驗證 ARC 簽章", "經 ARC 鏈轉送的驗證結果會以「宣稱」的形式交給 AI，並註明這一點。"),
            ("主機由你負責", "修補、磁碟加密、網路分段和異地備份屬於部署方的責任。"),
            ("判斷仍然可能出錯", "檢查擋得住沒有證據的答案，但不能讓模型變正確。所以處置一定要有人核准。"),
        ],
        report_h="回報弱點",
        report_p="發現部署中疑似的弱點時，請回報給該部署的 MARS 管理員，不要寫在公開的 issue。",
    ),
}

FAQ = {
    "en": dict(
        eyebrow="FAQ",
        h1="Questions people ask first.",
        lead="Short answers. The other pages have the detail.",
        groups=[
            ("Setting up", [
                ("What does MARS need to run?", "One host. MARS is a single service with a built-in database, so there is no separate database server or message broker to operate. The link sandbox is optional and runs in containers."),
                ("Which Microsoft services does it connect to?", "Microsoft 365 mail for the reporting mailbox, Defender XDR for incidents, Defender for Endpoint for device and email activity, and Entra ID for account context. You can also use MARS on uploaded message files alone."),
                ("How is it updated?", "With offline packages, so the host does not need internet access. Each package is verified, applied as a dry run first, and preceded by a backup."),
                ("Can I run more than one instance?", "No. MARS is designed as a single instance for one security team."),
            ]),
            ("AI", [
                ("Which models can it use?", "Anthropic, OpenAI and Gemini models, local models through Ollama or another local runtime, and OpenAI-compatible company gateways. Mail, XDR incidents, sandbox results and the analyst assistant can each use a different one."),
                ("Can it run without a cloud AI service?", "Yes. Point it at a local model or at a gateway inside your network. The host sets which endpoints MARS may reach."),
                ("What is sent to the model?", "The evidence MARS gathered for the case: header and body text, links, and the findings of its own checks. Internal mailboxes and account names can be replaced with pseudonyms before sending."),
                ("Can text in an email change the verdict?", "MARS is designed so that it should not. Attacker text is passed as marked evidence, the reply must fit a fixed format, and a conclusion that cites evidence MARS never collected is rejected. No defence here is absolute, which is why a person approves every action."),
                ("What happens when the AI is wrong?", "An answer without evidence behind it is held for review instead of published. Analysts can overrule a verdict and record why, and known cases are replayed before any change to the model or its instructions."),
            ]),
            ("Using it", [
                ("Does MARS take action by itself?", "No. It proposes response steps. A person approves them, and MARS then checks the outcome in the external system."),
                ("Which languages does the console support?", "Traditional Chinese and English. AI output is produced in English and translated into Traditional Chinese in the background."),
                ("What does it cost?", "MARS is free software under the GNU AGPL, version 3 or later. You pay for your own host and for the AI provider and threat-intelligence services you choose to connect."),
            ]),
        ],
    ),
    "zh": dict(
        eyebrow="常見問題",
        h1="大家最先問的問題。",
        lead="這裡是簡短的回答，細節在其他頁面。",
        groups=[
            ("安裝與維運", [
                ("MARS 需要什麼才能執行？", "一台主機。MARS 是單一服務加內嵌資料庫，不需要另外維運資料庫伺服器或訊息佇列。連結沙箱是選用的，以容器執行。"),
                ("它會連到哪些 Microsoft 服務？", "Microsoft 365 郵件（回報信箱）、Defender XDR（事件）、Defender for Endpoint（裝置與郵件活動），以及 Entra ID（帳號脈絡）。只用上傳的郵件檔也可以使用 MARS。"),
                ("怎麼更新？", "使用離線封包，主機不需要連上網際網路。每個封包都先驗證、先試套一次，套用前自動備份。"),
                ("可以跑多個實例嗎？", "不行。MARS 的設計是單一實例，給一個資安團隊使用。"),
            ]),
            ("AI", [
                ("可以用哪些模型？", "Anthropic、OpenAI、Gemini 的模型，透過 Ollama 或其他本機執行環境的本機模型，以及相容 OpenAI 介面的公司閘道。郵件、XDR 事件、沙箱結果和分析師助理可以各用不同的模型。"),
                ("可以不使用雲端 AI 服務嗎？", "可以。把它指向本機模型或內部網路裡的閘道即可。MARS 能連到哪些位址由主機設定。"),
                ("會把什麼送給模型？", "MARS 為這件案子收集到的證據：標頭與內文文字、連結，以及它自己各項檢查的結果。內部信箱和帳號名稱可以在送出前換成化名。"),
                ("郵件裡的文字能改變判定嗎？", "MARS 的設計目標是不能。攻擊者的文字以標記過的證據送出，回覆必須符合固定格式，引用了 MARS 沒收集到的證據的結論會被拒絕。這類防禦沒有絕對，所以每個處置都要有人核准。"),
                ("AI 判錯了怎麼辦？", "沒有證據支持的答案會被留下來複核，不會發佈。分析師可以推翻判定並記錄原因；更換模型或調整指示之前，會先重跑已知答案的案例。"),
            ]),
            ("使用", [
                ("MARS 會自己執行處置嗎？", "不會。它提出處置步驟，由人核准，之後再到外部系統確認結果。"),
                ("主控台支援哪些語言？", "繁體中文和英文。AI 的輸出以英文產生，在背景翻成繁體中文。"),
                ("費用是多少？", "MARS 以 GNU AGPL 第 3 版（或更新版本）授權釋出。你負擔的是自己的主機，以及你選擇串接的 AI provider 和威脅情資服務。"),
            ]),
        ],
    ),
}
