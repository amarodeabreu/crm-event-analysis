# $CRM Incident: Legal and Feasibility Issues

## Addendum to the Comprehensive Incident Timeline

**Date:** March 31, 2026
**Purpose:** This addendum identifies specific actions and claims that raise legal concerns or are technically infeasible, with cited sources for independent verification. This is not legal advice. It is a factual reference document identifying applicable statutes, legal standards, and technical constraints.

---

## A. Potentially Applicable Federal Statutes

### A.1: Wire Fraud (18 U.S.C. ss 1343)

**Statute:** "Whoever, having devised or intending to devise any scheme or artifice to defraud, or for obtaining money or property by means of false or fraudulent pretenses, representations, or promises, transmits or causes to be transmitted by means of wire, radio, or television communication in interstate or foreign commerce, any writings, signs, signals, pictures, or sounds for the purpose of executing such scheme or artifice, shall be fined under this title or imprisoned not more than 20 years, or both."

**Source:** https://www.law.cornell.edu/uscode/text/18/1343

**Elements required for wire fraud (per 9th Circuit Model Jury Instructions, Instruction 15.35):**

1. The defendant knowingly devised or participated in a scheme to defraud by means of false or fraudulent pretenses, representations, or promises
2. The false statements were material (capable of influencing a person to part with money or property)
3. The defendant acted with intent to deceive
4. Wire communications (internet, telephone) were used in furtherance of the scheme

**Source:** https://www.ce9.uscourts.gov/jury-instructions/node/1048

**Relevance to this matter:** Travis made public statements via Telegram and X (wire communications in interstate/foreign commerce) declaring the token "compromised" and instructing the community to "STOP BUYING," based on an investigation with documented factual errors (see Technical Counter-Analysis). These statements were material: community members made financial decisions based on them. Whether intent to deceive can be established is a question for investigators and prosecutors. The counter-analysis documents that the factual basis for the claims was demonstrably flawed.

**Penalty:** Up to 20 years imprisonment and/or fines per count. Each wire communication (each Telegram message, each X post) can constitute a separate count.

---

### A.2: Defamation Per Se (Civil)

**Legal standard:** Defamation per se involves false statements that are considered so inherently damaging that harm to reputation is automatically assumed without requiring additional proof of damages. Statements accusing someone of criminal conduct, dishonesty, or fraud are typically considered defamatory per se.

**Source:** Romano Law, "Understanding Business Torts": https://www.romanolaw.com/understanding-business-torts/

**Relevance to this matter:** Travis publicly accused specific community members of being part of a "criminal syndicate," "organized fraud," and "serial scammers" in a public Telegram group with 1,577 members and on X. These accusations are based on an investigation with documented factual errors. The accused community members have suffered documented financial harm ($70,000-$80,000 in one case). Accusing identifiable individuals of criminal conduct in a public forum, based on demonstrably flawed evidence, meets the standard elements of defamation per se in most jurisdictions.

---

### A.3: Tortious Interference with Business Relationships (Civil)

**Legal standard:** Tortious interference occurs when a third party intentionally and improperly disrupts a contract or business relationship between other parties, causing economic harm. Elements required: (1) a valid business relationship or expectancy, (2) the defendant's knowledge of it, (3) intentional and improper interference, (4) the interference caused damage.

**Source:** Minc Law, "What is Tortious Interference?": https://www.minclaw.com/tortious-interference/

**Relevance to this matter:** Community members held $CRM tokens and had reasonable expectations of continued participation in the project ecosystem. Travis's unsubstantiated public accusations and "STOP BUYING" directive directly interfered with these economic relationships, causing documented financial losses. The interference was based on claims that have been shown to contain multiple factual errors.

---

## B. Actions Without Legal Authority

### B.1: Demanding Wallet Disclosure

**What Travis did:** Demanded that community members and Amaro disclose their wallet addresses, and treated refusal or reluctance as evidence of wrongdoing.

**Legal reality:** Token holders on a public, permissionless blockchain have no legal obligation to disclose wallet addresses to a project founder, community member, or any private party. Only a court order, subpoena, or regulatory action from a body with statutory authority (such as the SEC, CFTC, DOJ, or a court of competent jurisdiction) can compel disclosure of financial information.

Travis has no subpoena power. Rug Munch Media LLC has no regulatory authority. A Wyoming LLC registration does not confer investigative or law enforcement powers.

**Implication:** Framing refusal to disclose wallet information as evidence of guilt, and using that framing to justify financial harm (blacklisting from airdrops, public accusations), has no legal basis.

### B.2: Unilateral Blacklisting and Asset Determination

**What Travis did:** Announced he would compile a blacklist of wallets excluded from the V2 airdrop, review it himself, and "entertain arguments" from those who dispute their inclusion.

**Legal reality:** Travis has appointed himself as investigator, prosecutor, judge, and appeals court over a process that determines who receives financial compensation and who does not. There is no independent oversight, no due process, and no legal framework authorizing this. The basis for the blacklist is an investigation with documented factual errors (confused token contracts, misidentified infrastructure wallets, empty wallets assigned high conviction ratings).

In contrast, legitimate token migration processes in the crypto industry typically involve either: (a) automatic on-chain snapshots with no exclusions, (b) independent third-party audits determining eligibility, or (c) community governance votes on disputed cases.

Travis has since stated that blacklisting decisions will be handled by a DAO with community voting on exclusions. However, the airdrop distribution that determines who holds V2 tokens, and therefore who can vote in the DAO, is itself controlled by Travis. If wallets are excluded from the airdrop based on the original investigation, those wallet holders cannot participate in the governance process meant to provide oversight of the exclusion list. The oversight mechanism is dependent on the decisions it is supposed to oversee.

### B.3: RICO Claims

**What Travis claimed:** Described his findings as constituting "RICO" evidence and stated the matter would be "turned over to the FBI as part of a rico case."

**Legal reality:** RICO (Racketeer Influenced and Corrupt Organizations Act, 18 U.S.C. ss 1961-1968) requires proof of: (1) an enterprise, (2) a pattern of racketeering activity (at least two predicate offenses within 10 years from a defined list including fraud, money laundering, extortion, etc.), (3) the defendant's participation in the enterprise through the pattern of racketeering activity.

**Source:** https://www.law.cornell.edu/uscode/text/18/part-I/chapter-96

Individuals trading tokens on a public DEX through an automated market maker is not racketeering activity. Multiple wallets interacting with the same liquidity pool is standard DeFi mechanics, not evidence of an enterprise. The RICO labels in Travis's report were generated by an AI chatbot in response to Travis's prompts, not by any legal authority or analysis.

---

## C. Technical Infeasibilities

### C.1: "1-to-1 Token Reimbursement" Without Platform Support

**What Travis promised:** "I will be implementing a 1-1 token reimbursement. Whatever the final structure looks like, the bottom line is this: you will receive the exact same number of tokens you held prior to this event occurring."

**Technical reality:** Travis has stated he will not use Bags.fm for V2. Creating a new token requires:

1. Deploying a new token mint on Solana (new contract address, no connection to V1)
2. Minting tokens for distribution
3. Creating and funding a liquidity pool
4. Distributing tokens to qualifying wallets via airdrop

The critical issue: a new token's value is determined by the liquidity in its pool, not by the number of tokens distributed. If Travis distributes 100M V2 tokens but the liquidity pool contains $100 of SOL, each token is worth $0.000001 regardless of what V1 was worth. "1-to-1 token count" is not "1-to-1 value reimbursement."

Travis plans to fund the liquidity pool with "a portion of the App revenue and a potential 1% trading fee." The app does not exist. There is no revenue. The liquidity funding depends on future income from products that have not been built by a person with no demonstrated ability to build them.

### C.2: "Deleted" Wallets as Evidence Destruction

**What Travis claimed:** That wallets being "deleted" (closed) after his investigation began constituted evidence destruction and cover-up activity.

**Technical reality:** On Solana, closing a token account removes the account's current state from the active ledger and reclaims the rent-exempt SOL deposit. However, the complete transaction history of every closed account remains permanently recorded in the blockchain's transaction ledger.

Any transaction the account ever participated in can be retrieved using standard Solana RPC methods:

- `getSignaturesForAddress` returns every transaction signature associated with an address
- `getTransaction` returns the full details of any transaction

Closing a Solana account does not delete, hide, or obscure any historical data. The claim that closing accounts "scrubs tracks" is technically incorrect.

Additionally, closing token accounts to reclaim rent-exempt SOL is routine user behaviour on Solana, commonly performed to recover small SOL deposits from dust token positions.

**Source:** Solana documentation on rent and account lifecycle: https://solana.com/docs/core/fees

### C.3: Delivering a Product Suite Within One Month

**What Travis promised:** "I hope to have the new product launched soon for you all within a month at the latest."

**The promised suite includes:** Airdrop checker, network and deep wallet forensics, first holders and gas funding tracking, advanced bundle checkers, in-house advanced bubble maps, smart money movers (market and specific tokens), DAO management system, "and many more features."

**Technical reality:** This is a description of a multi-product security analytics platform. Comparable products in the crypto security space (Nansen, Arkham, Bubblemaps, Chainalysis) were built by funded engineering teams over periods of months to years. The only functional tools in the CRM ecosystem to date (Marcus Aurelius bot, Rug Munch Intelligence, TG-Router) were built by Amaro, not Travis. Travis has no demonstrated record of building software products.

---

## D. Pattern of Materially False Public Statements

The following public statements can be verified as false or unsubstantiated based on the on-chain evidence documented in the Technical Counter-Analysis:

| Statement                                                                   | Where Made                        | Factual Status                                                                                                             | See                                   |
| --------------------------------------------------------------------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| An "organized fraud syndicate" infiltrated $CRM                             | Public announcement, X, Telegram  | No independently verified evidence published                                                                               | Counter-Analysis, all sections        |
| The syndicate drained "$11,000 from the community"                          | Public announcement               | No evidence published connecting specific wallets to coordinated extraction                                                | Counter-Analysis, Section 8           |
| Specific community members' wallets are connected to the syndicate via PBTC | Public and private communications | Based on confusion between two different tokens (PBTC TOKEN vs PBTC REWARD TOKEN)                                          | Counter-Analysis, Section 2           |
| "15-wallet criminal network" identified with 91-99% conviction              | Investigation report              | 10 of 14 wallets are empty; conviction ratings were assigned by AI chatbot without on-chain verification                   | Counter-Analysis, Section 8           |
| Forensic report to be delivered within 24-48 hours                          | Public announcement               | Not delivered as of March 31, 2026                                                                                         | Observable fact                       |
| "Our tools uncovered" the fraud                                             | Public announcement               | The tools (built by Amaro) did not produce these conclusions; Travis's own AI chatbot sessions did, with documented errors | Bot audit, Counter-Analysis Section 9 |
| Wallet closures represent evidence destruction                              | Private and public communications | Solana account closures do not delete transaction history; all data remains permanently queryable                          | Section C.2 above                     |

**Note on materiality:** These statements are material because community members made financial decisions based on them: holding tokens that Travis declared "essentially worthless," waiting for airdrops that depend on unfulfilled promises, and refraining from selling based on commitments of 1-to-1 reimbursement. Multiple community members have documented significant financial losses.

---

## E. Quantifiable Financial Harm

### E.1: Market Cap Destruction

The $CRM token's market capitalization dropped from above $200,000 to $6,684.44 (as verified on Solscan, March 31, 2026) following Travis's "URGENT Security Update" and "STOP BUYING" directive. This represents a destruction of over 96% of aggregate market value across all holders, triggered directly by Travis's public statements.

Travis himself described the tokens as "essentially worthless" in the public $CRM Chat on March 30.

### E.2: Individual Documented Losses

The combined self-reported loss for CM1 and Amaro is $70,000-$80,000.

**CM1 wallets (17):** On-chain verification confirms CM1 voluntarily disclosed 17 wallets (7 cluster, 10 separate). All 17 wallets currently hold 0 CRM. Full transaction history reconstructed via Helius Enhanced Transaction API: 604 CRM token transfers spanning August 26, 2025 through March 30, 2026. CM1 spent 544.52 SOL acquiring CRM and received 115.95 SOL selling, for a net loss of 428.57 SOL (~$55,700-$60,000 at $130-$140/SOL).

**Amaro wallets (3):** Three additional wallets held CRM tokens received from CM1 via direct token transfers:
- `8sPr8iXWB3qWCC7V82ffYydtqoNjqwHZq4TM4VfVzFBf`: received 10,000,000 CRM from CM1 Cluster #6 on Feb 28, 2026. Also received 10,000,000 CRM via intermediary wallet on Mar 1, 2026 (originally from CM1 Main Wallet via Wallet 2). Sold 5M CRM via DEX March 24-30.
- `7abBmGf4HNu3UXsanJc7WwAPW2PgkEb9hwrFKwCySvyL`: received 30,000,000 CRM from CM1 Main Wallet on Dec 31, 2025 (four transfers: 1M + 9M + 10M + 10M, verified on CM1's transaction history). Transferred 10M to intermediary wallet, sold remaining 20M CRM on Mar 31, 2026.
- `HCw8hKqSahdjY2y7UNubUyMBd521ZJUxB2Eg1VnbSz3W`: acquired 2,044,480 CRM via OKX DEX on Feb 13, 2026. Sold across March 24-30, 2026.

All three Amaro wallets currently hold 0 CRM. CRM was sold at depressed post-announcement prices across March 24-31, 2026 via OKX DEX Router, Jupiter, and DFlow. SOL proceeds from these DEX sells routed through wrapped SOL and are not fully captured in native transfer accounting.

**CM1 + Amaro combined (20 wallets):** 622 CRM token transfers total. The March 30 sell-off is clearly visible across both sets of wallets: CRM sold at severely depressed prices (e.g., 12,000,000 CRM for approximately 1 SOL, compared to approximately 600,000 CRM per SOL months earlier). The $70,000-$80,000 combined figure represents CM1's SOL investment in CRM (544.52 SOL, acquired at varying SOL prices over 7 months), plus Amaro's OKX purchase, minus the depressed-price sell proceeds recovered by both parties.

**CM2 wallets (23):** CM2 voluntarily disclosed 23 wallets, all Coinbase-funded: 1 Coinbase source wallet, 5 Axiom trading wallets, 1 BullX wallet, and 16 Phantom/Telegram bot wallets. The Phantom wallets held small CRM amounts (400-5,000 tokens each) for holder count diversity, a practice openly known and discussed among the whale community. Full transaction history reconstructed: 1,693 CRM token transfers. CM2 spent 185.73 SOL acquiring CRM and received 133.90 SOL selling, for a net loss of 51.83 SOL (~$6,700-$7,300 at $130-$140/SOL). Primary trading activity was concentrated in the four main Axiom wallets.

**All documented losses (43 wallets):** Combined on-chain verified losses across CM1 (17 wallets), Amaro (3 wallets), and CM2 (23 wallets): approximately $62,400-$67,300 in SOL-denominated losses. CM1 + Amaro self-reported $70,000-$80,000. Full results saved to cm1_loss_results.json.

Other community members have expressed losses but specific figures have not been documented for all holders.

### E.2.1: SOSANA Separation Verification

Travis's core accusation is that CM1, CM2, and Amaro are part of an organized SOSANA syndicate. On-chain verification of all 43 voluntarily disclosed wallets (17 CM1 + 3 Amaro + 23 CM2) directly disproves this:

**SOSANA token holdings:** Zero of 43 wallets hold any SOSANA tokens. Three CM2 trading wallets (Axiom #1, Axiom #3, BullX) have empty SOSANA token accounts (0 balance), indicating minor past speculative trades detailed below. The remaining 40 wallets (all 17 CM1, all 3 Amaro, and 20 of 23 CM2) have never had a SOSANA token account at all.

**Full disclosure of CM2's SOSANA activity (on-chain verified):**

CM2 Axiom #3 (`2cymcQGQz3fnTwW5FLQC8afDFm2yhC8h4kpUud1QB7Gf`):
- Nov 17, 2025 23:01-23:24: bought ~196.31 SOSANA via DEX (9 small fills)
- Nov 18, 2025 22:01: sold 190.41 SOSANA via DEX
- Held for approximately 1 day. Total exposure: ~196 tokens.

CM2 Axiom #1 (`E9bg6VCatYJGgrjADYbGdRF43HC3nqsFdqnQNk54oPpV`):
- Jan 6, 2026 20:39: bought 25.74 SOSANA via DEX
- Jan 7, 2026 21:23: sold 24.96 SOSANA via DEX (5 small fills)
- Held for approximately 1 day. Total exposure: ~26 tokens.

CM2 BullX (`CTjSDRDnTRu4634fHEUU9C6KmtYy3hwNr9Xc6atkEnqC`):
- Jan 6, 2026 20:34: bought 283.40 SOSANA via DEX
- Jan 6, 2026 22:17: bought 287.44 SOSANA via DEX
- Jan 8, 2026 12:16: bought 625.83 SOSANA via DEX
- Jan 10, 2026 16:41: sold 1,160.78 SOSANA via DEX (2 fills)
- Held for 2-4 days. Total exposure: ~1,197 tokens.

Combined SOSANA exposure across all three wallets: approximately 1,419 tokens, held 1-4 days each, all fully sold. For context, the #1 SOSANA holder alone owns 32,920,508 tokens. CM2's entire historical SOSANA exposure was 0.004% of that single holder's position. These were minor speculative trades conducted via public DEX, not coordinated syndicate activity.

**Connection to top SOSANA holders:** The top 10 SOSANA holders control 80.13% of the token supply. Transaction history analysis of the three CM2 wallets with past SOSANA activity shows zero transactions with any of these top holders. All SOSANA trades were conducted via DEX liquidity pools with no direct counterparty overlap.

**Top 10 SOSANA holders (for reference):**

| Rank | Address | Balance | % Supply |
|------|---------|---------|----------|
| 1 | `CPJAPpJ9DE7fxw8aSTnDNafGLDPdbw7ewntJFkvkUvDG` | 32,920,508.93 | 37.04% |
| 2 | `CPJAPpJ9DE7fxw8aSTnDNafGLDPdbw7ewntJFkvkUvDG` | 22,398,110.92 | 25.20% |
| 3 | `3abEJKNprMq7vfTb4wKi41DRfxgMquS31m5TgUKEoNxG` | 8,880,897.08 | 9.99% |
| 4 | `4pxuEZQ5boEN31c3QrgBHW1fAC6Msv3GRq8E7drs5svD` | 1,287,240.56 | 1.45% |
| 5 | `F3L4SHtoa2pnf5tmaeY6pZuoP7e1YThfu7FeTS3RCNR2` | 1,263,557.50 | 1.42% |
| 6 | `DnwGW4SMvLeJFrinM7AksiicxfSmpNteLWWT3B59ijw4` | 1,249,966.25 | 1.41% |
| 7 | `FgHBe4FmCTfrKuaQeWMf6EtUpRyGv38XzuPG2rGM781i` | 1,209,186.74 | 1.36% |
| 8 | `B7zwDzjSh6rQgZUUrV6F2NngvX6fShaRT3q4BA1dNhp7` | 1,104,651.13 | 1.24% |
| 9 | `BYWWdCyzkK93rmQRXYkx8anfVW7Gx4geLMPoUYYVMH7T` | 989,649.29 | 1.11% |
| 10 | `F4HGHWyaCvDkUF88svvCHhSMpR9YzHCYSNmojaKQtRSB` | 810,751.45 | 0.91% |

None of these addresses appear in any transaction across any of the 43 community wallets. The claim that CM1, CM2, or Amaro are connected to SOSANA has zero on-chain evidence.

### E.3: CFTC Jurisdiction Over Commodity Market Manipulation

Cryptocurrencies are considered commodities under the Commodity Exchange Act (CEA), granting regulatory authority to the Commodity Futures Trading Commission (CFTC). Section 9 of the CEA specifically prohibits "disseminating knowingly false or reckless information to influence prices."

**Source:** The Bulldog Law, "Cryptocurrency Market Manipulation: Legal Risks Under the Commodity Exchange Act": https://www.thebulldog.law/cryptocurrency-market-manipulation-legal-risks-under-the-commodity-exchange-act

Civil penalties under the CEA can reach up to $1,000,000 per violation or triple the gains derived from misconduct.

**Relevance:** Travis publicly instructed 1,577 community members to "STOP BUYING" the token and declared it "compromised," based on claims of a "syndicate" infiltration. If these claims were made recklessly (without adequate verification) or knowingly (despite awareness of the factual errors), they may constitute dissemination of false information to influence price under the CEA.

---

## F. Accountability Summary: Observable Facts

The following is a factual summary derived from documented evidence:

| Observable Fact                                                                       | What It Demonstrates                                                                                    | Evidence Source                      |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| Investigation confused two different PBTC tokens                                      | Factual basis for accusing CM1 of syndicate membership is flawed                                        | On-chain mint address verification   |
| 10 of 14 "criminal network" wallets are empty                                         | The network report is unsubstantiated                                                                   | On-chain balance queries             |
| Travis told community to "STOP BUYING"                                                | Directly suppressed the token's market                                                                  | Public Telegram/X post               |
| Market cap fell from above $200K to $6,684 (96%+ destruction)                         | Statements caused measurable financial harm to all holders                                              | Solscan, on-chain and DEX chart data |
| Travis stated tokens are "essentially worthless" while promising future airdrop       | Holders asked to hold worthless assets based on future promises from entity with no EIN or bank account | Public $CRM Chat messages            |
| Forensic report promised in 24-48 hours                                               | Not delivered as of March 31                                                                            | Observable fact                      |
| App suite promised "within a month"                                                   | No demonstrated technical ability to deliver; sole technical contributor stepped back                   | Private Whales message               |
| LLC has no EIN, uses virtual mailbox                                                  | Entity backing all commitments has no operational financial infrastructure                              | Wyoming Secretary of State filing    |
| Amaro warned Travis of PBTC/CRM token confusion on March 27                           | Travis was aware of methodology flaws before making public claims                                       | Private Telegram messages            |
| Travis called CM1 "a legend" on March 14; accused CM1 of being a criminal on March 27 | No change in CM1's behaviour; change was Travis's failed negotiation                                    | Private Telegram messages            |
| Travis proposed criminal operations in "Dark Paper"                                   | Character and intent are relevant to evaluating his claims about others                                 | Private Telegram messages            |
| Travis agreed to coordinate step-back announcement                                    | Published unilaterally without coordinating                                                             | Private Telegram messages            |
| Multiple community members asked for evidence                                         | Travis responded "I will reveal none at the present time"                                               | Public $CRM Chat screenshots         |
| Travis told CM1 to "Stfu" in public chat                                              | Response to legitimate criticism from the project's largest financial supporter                         | Public $CRM Chat screenshot          |

---

*This document identifies applicable legal standards and technical constraints based on publicly available legal sources and blockchain documentation. It is not legal advice. Individuals who believe they have been harmed should consult with a qualified attorney in the relevant jurisdiction.*
