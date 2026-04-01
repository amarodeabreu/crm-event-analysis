# $CRM On-Chain Counter-Analysis

## Independent Verification of Claims Made in the March 30, 2026 "URGENT Security Update"

**Date:** March 31, 2026
**Methodology:** All on-chain data verified via Solana mainnet RPC and Helius API. All wallet addresses and contract addresses are provided so that any party can independently reproduce these results.
**Scope:** This document examines the factual claims made in the public announcement regarding an alleged "coordinated attack by an organized fraud syndicate" targeting the $CRM token.

---

## 1. Summary of Findings

The public announcement made the following core claims:

1. A coordinated fraud syndicate infiltrated $CRM during its stealth launch.
2. The syndicate acquired approximately 30% of token supply.
3. The syndicate systematically dumped tokens through a web of small wallets, draining approximately $11,000.
4. Specific community members' wallets are connected to this syndicate via the SOSANA project and a token called PBTC.

**This counter-analysis finds that each of these claims is based on verifiable factual errors, including confused token contract addresses, misidentified infrastructure wallets, and unverified assertions.**

---

## 2. Error #1: PBTC Token Confusion (Two Different Tokens)

The central claim connecting community members to the alleged SOSANA syndicate relies on the assertion that holding "PBTC" tokens proves membership in a criminal network.

There are two entirely separate tokens both using the PBTC ticker on Solana. These are not the same token. They have different mint addresses, different creators, different supply structures, and different purposes:

| Attribute | PBTC TOKEN (Purple Bitcoin) | PBTC REWARD TOKEN ("Pruple Bitcoin": note misspelling in on-chain metadata) |
|-----------|---------------------------|-----------------------------------------------------------------------------|
| **Mint Address** | `HfMbPyDdZH6QMaDDUokjYCkHxzjoGBMpgaUvpLWGbF5p` | `EysSQoB4pL22cuSk9uajYgRNgCqPo3qDMxkwK5GWaAUi` |
| **Total Supply** | ~21,000,000 | ~100,000,000,000 |
| **Distribution** | Traded on DEX, dispersed holders (healthy distribution) | 91% held by single address (airdrop/reward distribution pattern) |
| **Creator Authority** | `AX6c3wzF...` | `GeArrhSj...` |
| **Nature** | Independent community token traded on open market | Reward/distribution token associated with a specific project |

The investigation's claim that "if someone holds PBTC they are part of their extraction network" conflates these two tokens. The community member in question (wallet `8eVZa7bEBnd6MA6JJkNdABRN4S3LbVLRnCZNJAUeuwQj`) holds the **PBTC TOKEN (Purple Bitcoin)**, a retail purchase on a public DEX representing 0.26% of that token's supply (50,001.89 tokens). This is a small retail position consistent with a market buy. It is not the PBTC REWARD TOKEN that the investigation associates with SOSANA.

**Verification:** Query `getTokenAccountsByOwner` on wallet `8eVZa7...` and compare the returned token mint against both addresses above. The mint address will match the PBTC TOKEN (`HfMbPy...`), not the PBTC REWARD TOKEN (`EysSQo...`).

---

## 3. Error #2: Wrong Wallet Attributed to Community Member

While the investigation examined multiple wallets, at least one key wallet: `HConWUDnXbTy5Hy7M1QeSYuvv8puMjkJNsFcTmbK8JXx`: was incorrectly attributed to a specific community member and used to draw conclusions about that person's activity and alleged network connections.

The community member's actual wallet is `8eVZa7bEBnd6MA6JJkNdABRN4S3LbVLRnCZNJAUeuwQj`, which was publicly shared by the wallet owner in group chat and is verifiable. Any conclusions drawn from the misattributed wallet cannot be applied to this community member.

**Note on wallet privacy:** Token holders on a public, permissionless blockchain have no obligation to disclose wallet addresses to other community members or project founders. Refusal to share a wallet address is not evidence of wrongdoing. Participants in an open market are free to buy and sell tokens at their discretion.

---

## 4. Error #3: SOSANA Contract Address Confusion

The investigation referenced contract address `FLGhyMsFtr8mCFGaLuFhs7VNUqZgNaZ7YFkurPKKpump` as the SOSANA token.

On-chain metadata for this address identifies it as **"Nietzschean Dog ($DOG)"**, a pump.fun memecoin entirely unrelated to SOSANA.

The actual SOSANA token is:

| Attribute | Value |
|-----------|-------|
| **Mint** | `49jdQxUkKtuvorvnwWqDzUoYKEjfgroTzHkQqXG9YFMj` |
| **Symbol** | SOSANA |
| **Supply** | 88,888,887.79 |
| **Authority** | `F4HGHWyaCvDkUF88svvCHhSMpR9YzHCYSNmojaKQtRSB` |

The three relevant token authorities are entirely separate with zero overlap:

| Token | Creator/Authority |
|-------|------------------|
| PBTC (Purple Bitcoin) | `AX6c3wzF...` |
| PBTC Reward Token | `GeArrhSj...` |
| SOSANA | `F4HGHW...` |

**Verification:** Query `getAccountInfo` on each mint address and compare the authority fields.

---

## 5. Error #4: Second Community Member Has Zero Relevant Holdings

Wallet `BKLBtcJQJ2MxJP6wfbRkoqrYNWUPVLfeB8vs91agBxjt` was accused of being connected to the SOSANA syndicate.

On-chain verification (March 30, 2026):

| Check | Result |
|-------|--------|
| SOL Balance | 0.003440 SOL |
| Token Accounts | 1 (not PBTC, not SOSANA) |
| PBTC Holdings | 0 |
| PBTC Reward Holdings | 0 |
| SOSANA Holdings | 0 |
| Direct transactions with first community member's wallet (last 50 tx) | 0 |
| Presence in top 20 holders of PBTC, PBTC Reward, or SOSANA | No |

This wallet has zero connection to any of the tokens cited in the accusation. Not a single transaction.

**Verification:** Query `getBalance` and `getTokenAccountsByOwner` on `BKLBtcJQ...` and scan transaction history via `getSignaturesForAddress`.

---

## 6. Error #5: DEX Liquidity Pool Misidentified as Criminal Wallet

The investigation identified wallet `HLnpSz9h2S4hiLQ4mxtAYJJQXx9USzEXbte2RVP9QEd` as a "Feeder + Dumper" wallet that allegedly loaded 20M CRM via internal transfers and dumped on March 26.

This address appears as a counterparty in virtually every CRM trade because it is a **DEX automated market maker (AMM) liquidity pool routing wallet**. When any user buys CRM on a decentralized exchange, this wallet is the counterparty. When any user sells CRM, this wallet is the counterparty. This is standard AMM mechanics.

The investigation observed that both community members transacted with this wallet and concluded they were part of the same network. By this logic, every person who has ever traded CRM on a DEX is a member of the same "criminal network," because all trades route through the same pool.

**Note:** The investigator did correctly identify a separate infrastructure wallet misidentification during the investigation, the Raydium Liquidity Pool V4 Authority (`5Q544fKrFoe6tsEbD7S8EmxGTJYAKtTVhAW5Q5pge4j1`) was initially flagged as suspicious before being recognized as a core protocol address. However, the same type of error was not caught for `HLnpSz9h...`, which remained classified as a criminal wallet in the final report despite being DEX infrastructure.

**Verification:** Examine any CRM swap transaction on Raydium or Jupiter and observe that `HLnpSz9h...` appears as a party.

---

## 7. Error #6: Metadata Authority Misidentified as Treasury

The investigation called wallet `F4HGHWyaCvDkUF88svvCHhSMpR9YzHCYSNmojaKQtRSB` the "SOSANA v2 Treasury — Root controller" and assigned it the highest tier in the alleged criminal network hierarchy.

This address is the SOSANA token's **Metaplex metadata update authority**. This key can update the token's name, symbol, and image on Solana's metadata standard. It cannot move tokens, cannot control funds, and is not a treasury.

On-chain balance as of March 30, 2026: 3.3 SOL and a handful of miscellaneous tokens. No PBTC. No CRM.

**Verification:** Query the SOSANA token mint's metadata account and compare the `updateAuthority` field against this address.

---

## 8. Error #7: Empty Wallets Assigned High Conviction Ratings

Of the 14 wallets listed in the alleged "criminal network" with conviction ratings of 91-99%:

| Category | Count | Details |
|----------|-------|---------|
| Completely empty (0 SOL, 0 tokens) | 10 | Including wallets labeled "Primary Dump Wallet — extracted $740K" and "Master Routing Node" and "Core Cluster Leader — 104.6M CRM dormant" |
| Minimal balance (dust only) | 2 | Under 0.3 SOL, no meaningful token holdings |
| Active with holdings | 1 | The community member's legitimate whale wallet |
| Metadata authority (not a treasury) | 1 | See Error #6 above |

A conviction rating of 98% on a wallet currently holding zero SOL and zero tokens requires explanation. If these wallets held significant assets at the time of investigation, transaction history would show those movements and is publicly auditable.

**Verification:** Query `getBalance` and `getTokenAccountsByOwner` on each address. For historical verification, use `getSignaturesForAddress` to pull the complete transaction history and determine whether these wallets ever held the claimed assets.

**Note on Solana's permanent ledger:** Even when wallets are emptied or token accounts are closed, the complete transaction history remains permanently recorded and publicly queryable. Any claim about past holdings can be verified against the historical record. If these wallets held the claimed assets and subsequently moved them, those transactions are visible. If they never held the claimed assets, that is also visible.

---

## 9. Error #8: Unverified AI Output Used as Basis for Public Accusations

The investigation was conducted primarily through AI chatbot sessions. AI chatbots are tools with known limitations, they can speculate, hallucinate, and produce confident-sounding output that is factually incorrect. The responsibility for verifying AI output before acting on it rests with the human operator.

Key facts documented in the bot infrastructure server logs:

- The bots stamped outputs with "[ON-CHAIN: 100%]" labels on claims that were not independently verified via RPC calls. This is a bot behaviour limitation, not a verification of accuracy.
- 69 scan API calls failed during the investigation period, causing the bot to fall back to LLM-only responses that appear identical in format to real scan data but contain no verified on-chain information. The investigator continued to rely on these outputs.
- When the investigator pasted the bot's own prior output back as a new prompt, the bot confirmed its own text: creating a self-referencing validation loop. This is expected AI behaviour, not independent verification.
- The bots explicitly stated they could not perform multi-hop wallet tracing or prove wallet connections. The investigator proceeded regardless.

**The core issue is not that the bots produced errors: AI tools regularly do. The issue is that unverified AI output was used as the sole basis for public accusations of criminal activity, causing financial harm to identifiable individuals, without the investigator performing independent on-chain verification using readily available tools (Solana RPC, Helius API, Solscan, etc.).**

No independently verified on-chain evidence supporting the "criminal syndicate" claims has been published to date, despite a stated deadline of 24-48 hours from the initial announcement.

**Verification:** The complete bot interaction logs, including timestamps and message content, are available from the bot infrastructure operator and can be provided to any independent reviewer or legal authority.

---

## 10. Clarification: "Deleted" Wallets Are Still Fully Auditable

The public announcement stated: "As soon as I started my audit, they began closing Solana accounts to scrub their tracks."

On Solana, closing a token account reclaims the rent-exempt SOL deposit and removes the account's current state from the active ledger. However, **every transaction that account ever participated in remains permanently recorded in the blockchain's transaction history.** Closing an account does not "scrub tracks", it is a routine operation that token holders perform regularly to reclaim SOL from unused token accounts.

The complete history of any closed account can be reconstructed using `getSignaturesForAddress`, which returns every transaction signature associated with that address regardless of whether the account is currently open or closed. Each transaction can then be examined in full detail using `getTransaction`.

If these wallets held the assets claimed by the investigation, the on-chain record will show it. If they never held those assets, the record will show that too. Either way, the data is permanent and publicly accessible.

**Verification:** Run `getSignaturesForAddress` on any of the wallet addresses listed in Section 11 to retrieve the complete transaction history.

---

## 11. Clarification: RICO and Criminal Enterprise Claims

The investigation's report assigns "RICO" classifications and "criminal enterprise" labels to wallet activity. For context:

RICO (the Racketeer Influenced and Corrupt Organizations Act) requires proof of a pattern of racketeering activity conducted through an enterprise, involving predicate offenses such as fraud, money laundering, extortion, or other specific federal crimes. The statute has a high evidentiary bar and is prosecuted by the U.S. Department of Justice.

Individuals trading tokens on a public, permissionless decentralized exchange: buying and selling at market price through an automated market maker: does not constitute racketeering activity. Multiple wallets interacting with the same DEX liquidity pool is not evidence of coordination; it is the normal functioning of decentralized finance infrastructure.

The labels "RICO," "criminal enterprise," "syndicate," and similar characterizations in the investigation's report are not legal determinations. They are labels applied by an AI chatbot in response to prompts from the investigator.

---

## 12. Methodology Note

This counter-analysis uses exclusively:

- Solana mainnet RPC queries (`getBalance`, `getTokenAccountsByOwner`, `getAccountInfo`, `getSignaturesForAddress`)
- Helius API for enhanced transaction data
- On-chain token metadata (Metaplex)
- Public DEX and protocol documentation (Raydium, Jupiter)
- Bot infrastructure server logs (timestamps, message routing, API failure records)

No speculative analysis, pattern matching, or inference is used. Every claim in this document can be independently verified by any party with access to a Solana RPC endpoint.

---

## 12a. Context: What the Investigation "Discovered" Was Common Knowledge

The following information, presented in the investigation as covert discoveries, was openly known and discussed among the $CRM whale community for months prior to the investigation:

| "Discovery" | Actual Status |
|------------|---------------|
| CM1 is the largest CRM whale | Known by the entire community. CM1's position was openly discussed and the investigator himself described CM1 as "a legend" and "major backer" on March 14, 2026. |
| CM1 holds PBTC | CM1 discussed his PBTC investment openly in the whale group. |
| CM1 introduced Amaro to the project | No secret. The investigator discussed this directly with Amaro on March 14: "Great of him to introduce you." |
| Amaro built the Marcus bot and tools | Obviously known: Amaro was the project's sole technical contributor. |
| CM2 sold CRM in December | CM2 never denied this. CM2 sold after the investigator left for an extended trip to Asia, then bought back at a loss. This was visible on-chain and discussed openly. |
| Multiple community members use multiple wallets | A known and discussed practice among the whale group to avoid wallet clustering and maintain holder count diversity. |
| Whale wallet addresses are "connected" | The whale group actively shared and tracked each other's wallet addresses as a community practice. Known wallets included those belonging to CM1, CM2, and several other named community members. |

The investigation repackaged openly known community information through AI chatbot sessions that added speculative "connections," criminal language, and conviction percentages: then presented the output as covert forensic discoveries warranting a public emergency announcement.

No new information has been produced by the investigation that was not already known to the whale community.

---

## 13. Wallet Address Reference

For independent verification, the following addresses are referenced in this document:

| Label | Address |
|-------|---------|
| Community Member 1 Wallet | `8eVZa7bEBnd6MA6JJkNdABRN4S3LbVLRnCZNJAUeuwQj` |
| Community Member 2 Wallet | `BKLBtcJQJ2MxJP6wfbRkoqrYNWUPVLfeB8vs91agBxjt` |
| Wrong Wallet (attributed to Member 1) | `HConWUDnXbTy5Hy7M1QeSYuvv8puMjkJNsFcTmbK8JXx` |
| PBTC: Purple Bitcoin (real) | `HfMbPyDdZH6QMaDDUokjYCkHxzjoGBMpgaUvpLWGbF5p` |
| PBTC Reward Token (different token) | `EysSQoB4pL22cuSk9uajYgRNgCqPo3qDMxkwK5GWaAUi` |
| SOSANA Token Mint | `49jdQxUkKtuvorvnwWqDzUoYKEjfgroTzHkQqXG9YFMj` |
| SOSANA Metadata Authority | `F4HGHWyaCvDkUF88svvCHhSMpR9YzHCYSNmojaKQtRSB` |
| DEX/AMM Pool Routing Wallet | `HLnpSz9h2S4hiLQ4mxtAYJJQXx9USzEXbte2RVP9QEd` |
| Raydium LP V4 Authority | `5Q544fKrFoe6tsEbD7S8EmxGTJYAKtTVhAW5Q5pge4j1` |
| $DOG Token (misidentified as SOSANA) | `FLGhyMsFtr8mCFGaLuFhs7VNUqZgNaZ7YFkurPKKpump` |
| CRM Token Mint | `Eme5T2s2HB7B8W4YgLG1eReQpnadEVUnQBRjaKTdBAGS` |

---

*This document contains no editorial commentary. It presents verifiable on-chain data and identified factual errors. All addresses are provided for independent verification. Any party can reproduce these findings using a Solana RPC endpoint.*
