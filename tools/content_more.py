# Copy for the Security and FAQ pages.

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
            ("Licence", [
                ("What does the AGPL allow?", "You may run MARS, read its source, change it and pass it on, for any purpose and at no charge. The licence comes with no warranty."),
                ("What does it ask of us in return?", "If you run a modified MARS for people who use it over a network, section 13 of the licence requires you to offer those people the source of your modified version. If you distribute MARS, changed or not, it stays under the same licence. Running MARS unmodified adds no publishing duty."),
                ("Do we have to publish our settings or data?", "No. The licence covers the program. Your configuration, the mail MARS analyses and the records it keeps are yours and are not source code."),
                ("Does the licence cover everything MARS ships with?", "MARS depends on components with their own copyleft licences, among them PyMuPDF (AGPL-3.0) and extract-msg and pcodedmp (GPL-3.0). The dependency list in the repository names all of them."),
                ("Is this page legal advice?", "No. It is a summary. The licence text is what binds, so read it, and ask your own counsel if the terms matter to a decision."),
            ]),
        ],
    ),
}
