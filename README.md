# $CRM On-Chain Counter-Analysis

## Independent Verification of Claims Made in the March 30, 2026 "URGENT Security Update"

On March 30, 2026, the founder of the $CRM (Crypto Rug Muncher) project published a public announcement declaring the token "compromised," instructing the community to "STOP BUYING," and accusing specific community members of being part of an "organized fraud syndicate" connected to the SOSANA project via a token called PBTC.

This repository contains an independent on-chain verification of those claims. Every finding can be reproduced by anyone with access to a Solana RPC endpoint.

**The market cap of $CRM fell from above $200,000 to $6,684 following these announcements, a destruction of over 96% of aggregate market value.**

---

## Summary of Findings

The investigation's claims are based on the following verifiable factual errors:

| # | Error | Description |
|---|-------|-------------|
| 1 | **PBTC Token Confusion** | Two different tokens share the PBTC ticker. The PBTC TOKEN (Purple Bitcoin, mint `HfMbPy...`, ~21M supply) is a separate project from the PBTC REWARD TOKEN (`EysSQo...`, ~100B supply). The accused community member holds the former: a retail purchase, not a reward distribution. |
| 2 | **Wrong Wallet Attributed** | At least one wallet was incorrectly attributed to a community member and used to draw conclusions about that person. |
| 3 | **SOSANA Contract Confusion** | The address cited as SOSANA (`FLGhy...pump`) is actually "Nietzschean Dog ($DOG)": an unrelated pump.fun memecoin. |
| 4 | **Zero Relevant Holdings** | A second accused community member's wallet has zero PBTC, zero SOSANA, and zero relevant token transactions. |
| 5 | **DEX Pool Misidentified** | A DEX/AMM liquidity pool routing wallet was classified as a "Feeder + Dumper" criminal wallet. All CRM trades route through this address. |
| 6 | **Metadata Authority != Treasury** | The SOSANA token's Metaplex metadata update authority was labeled "SOSANA v2 Treasury — Root controller." It cannot move funds. |
| 7 | **Empty Wallets with High Conviction** | 10 of 14 wallets in the alleged "criminal network" are completely empty (0 SOL, 0 tokens), yet assigned conviction ratings of 91-99%. |
| 8 | **Unverified AI Output** | The investigation was conducted via AI chatbot sessions. 69 scan API calls failed, causing LLM-only fallback responses that looked like real data. The AI confirmed its own prior output when it was pasted back. |

Full details: [CRM_Technical_Counter_Analysis.md](./CRM_Technical_Counter_Analysis.md)

---

## Important Context: Nothing Was "Discovered"

The information presented in the investigation as covert discoveries was openly known and discussed among the $CRM whale community for months:

- CM1 being the largest whale was known by everyone. The investigator called CM1 "a legend" and "major backer" on March 14, 2026: thirteen days before accusing CM1 of being a criminal.
- CM1's PBTC investment was discussed openly in the whale group.
- CM1 introducing the project's technical contributor was no secret, the investigator discussed it directly with the contributor.
- CM2 selling CRM in December was never denied and was visible on-chain. CM2 sold after the investigator left for an extended trip and bought back at a loss.
- Multiple community members using multiple wallets was a known and discussed practice to avoid clustering and maintain holder count diversity.
- Whale wallet addresses were actively shared and tracked among the community.

The investigation repackaged this openly known information through AI chatbot sessions that added speculative connections, criminal language, and conviction percentages, then presented the output as covert forensic discoveries warranting a public emergency announcement that crashed the token by over 96%.

---

## Repository Contents

```
crm-analysis/
|-- README.md                              # This file
|-- CRM_Technical_Counter_Analysis.md      # Full counter-analysis document
|-- CRM_Comprehensive_Incident_Timeline.md # Incident timeline with parties, evidence index
|-- CRM_Legal_Issues_Addendum.md           # Legal issues addendum (statutes, losses, governance)
|-- verify_claims.py                       # Automated verification of all claims
|-- cm1_loss_verification.py               # CM1 + Amaro historical CRM loss reconstruction
|-- compare_pbtc_tokens.py                # PBTC TOKEN vs PBTC REWARD TOKEN comparison
|-- wallet_history.py                      # Transaction history for any wallet
|-- cm1_loss_results.json                  # Full transaction data (622 CRM transfers, 20 wallets)
|-- files/                                 # Evidence screenshots (E01 through E25)
```

---

## Quick Start

### Requirements

- Python 3.8+
- `requests` library

```bash
pip install requests
```

No API key is required for basic verification. The scripts use the public Solana mainnet RPC by default. For faster queries and higher rate limits, you can optionally provide a Helius API key.

### Run All Verifications

```bash
python3 verify_claims.py
```

This will query live Solana mainnet data and verify each claim from the counter-analysis, including:

- PBTC TOKEN vs PBTC REWARD TOKEN (different mint addresses)
- CM1's actual token holdings (PBTC TOKEN, not REWARD TOKEN)
- CM2's wallet (zero PBTC, zero SOSANA)
- SOSANA metadata authority balance (not a treasury)
- All 14 "criminal network" wallets (balance check)
- DEX pool identification

With a Helius API key (faster, higher rate limits):

```bash
python3 verify_claims.py --helius YOUR_API_KEY
```

### Verify CM1 + Amaro CRM Losses

```bash
# Requires Helius API key
python3 cm1_loss_verification.py --helius YOUR_API_KEY --output cm1_loss_results.json

# Or via environment variable
export HELIUS_API_KEY=YOUR_API_KEY
python3 cm1_loss_verification.py --output cm1_loss_results.json
```

Reconstructs full CRM transaction history across all 20 wallets (17 CM1 + 3 Amaro), calculates SOL spent vs received, and outputs a chronological timeline of all 622 CRM token transfers.

### Compare PBTC Tokens

```bash
python3 compare_pbtc_tokens.py
```

Detailed comparison showing these are two entirely different tokens with different mints, different supplies, different authorities, and different creators.

### Check Any Wallet's Transaction History

```bash
# Basic usage (last 100 transactions)
python3 wallet_history.py WALLET_ADDRESS

# More transactions
python3 wallet_history.py WALLET_ADDRESS --limit 500

# Save full results to JSON
python3 wallet_history.py WALLET_ADDRESS --output history.json

# With Helius API for better rate limits
python3 wallet_history.py WALLET_ADDRESS --helius YOUR_API_KEY
```

This script is particularly relevant for the "deleted wallet" claim. On Solana, closing a token account does NOT delete its transaction history. Every transaction is permanent and publicly queryable. You can run this script on any closed/empty wallet to see its complete activity history.

---

## Wallet Address Reference

All addresses referenced in the analysis, provided for independent verification:

| Label | Address |
|-------|---------|
| Community Member 1 (CM1) Main Wallet | `8eVZa7bEBnd6MA6JJkNdABRN4S3LbVLRnCZNJAUeuwQj` |
| CM2 Coinbase Source | `GEiTi7Qf6gZT4QinNbm29o7Skstb5jTRgB1C8y1io4MR` |
| CM2 Axiom #1 | `E9bg6VCatYJGgrjADYbGdRF43HC3nqsFdqnQNk54oPpV` |
| CM2 Axiom #2 | `EQGuHysoEdjnk7sst8WqK8BZEmju8VhUf52xmmueYTUa` |
| CM2 Axiom #3 | `2cymcQGQz3fnTwW5FLQC8afDFm2yhC8h4kpUud1QB7Gf` |
| CM2 Axiom #4 | `BKLBtcJQJ2MxJP6wfbRkoqrYNWUPVLfeB8vs91agBxjt` |
| CM2 Axiom #5 | `5Mi553gMwXHFw2nAKxNt7WWDvoLYr5aAE3xMDHELMzan` |
| CM2 BullX | `CTjSDRDnTRu4634fHEUU9C6KmtYy3hwNr9Xc6atkEnqC` |
| Wrong Wallet (attributed to CM1) | `HConWUDnXbTy5Hy7M1QeSYuvv8puMjkJNsFcTmbK8JXx` |
| Amaro Wallet #1 | `8sPr8iXWB3qWCC7V82ffYydtqoNjqwHZq4TM4VfVzFBf` |
| Amaro Wallet #2 | `7abBmGf4HNu3UXsanJc7WwAPW2PgkEb9hwrFKwCySvyL` |
| Amaro Wallet #3 | `HCw8hKqSahdjY2y7UNubUyMBd521ZJUxB2Eg1VnbSz3W` |
| PBTC TOKEN (Purple Bitcoin) | `HfMbPyDdZH6QMaDDUokjYCkHxzjoGBMpgaUvpLWGbF5p` |
| PBTC REWARD TOKEN (different token) | `EysSQoB4pL22cuSk9uajYgRNgCqPo3qDMxkwK5GWaAUi` |
| SOSANA Token Mint | `49jdQxUkKtuvorvnwWqDzUoYKEjfgroTzHkQqXG9YFMj` |
| SOSANA Metadata Authority | `F4HGHWyaCvDkUF88svvCHhSMpR9YzHCYSNmojaKQtRSB` |
| DEX/AMM Pool Routing Wallet | `HLnpSz9h2S4hiLQ4mxtAYJJQXx9USzEXbte2RVP9QEd` |
| Raydium LP V4 Authority | `5Q544fKrFoe6tsEbD7S8EmxGTJYAKtTVhAW5Q5pge4j1` |
| $DOG Token (misidentified as SOSANA) | `FLGhyMsFtr8mCFGaLuFhs7VNUqZgNaZ7YFkurPKKpump` |
| CRM Token Mint | `Eme5T2s2HB7B8W4YgLG1eReQpnadEVUnQBRjaKTdBAGS` |

CM1 voluntarily disclosed 17 wallets (7 cluster, 10 separate). Amaro's 3 wallets held CRM received from CM1 via direct token transfers. CM2 voluntarily disclosed 23 wallets (all Coinbase-funded), including 16 Phantom wallets with small CRM amounts for holder count diversity. Full addresses in `verify_claims.py`. On-chain verified losses: CM1 + Amaro $70,000-$80,000 (self-reported), CM2 ~$6,700-$7,300. Transaction data in `cm1_loss_results.json`.

You can verify any of these on [Solscan](https://solscan.io) by pasting the address into the search bar.

---

## How to Verify Manually (No Scripts Required)

If you prefer not to run code, you can verify every claim using Solscan:

1. **PBTC Token Confusion**: Search `HfMbPyDdZH6QMaDDUokjYCkHxzjoGBMpgaUvpLWGbF5p` and `EysSQoB4pL22cuSk9uajYgRNgCqPo3qDMxkwK5GWaAUi` on Solscan. Note they are different tokens with different supplies and creators.

2. **CM2's Holdings**: Search `BKLBtcJQJ2MxJP6wfbRkoqrYNWUPVLfeB8vs91agBxjt` on Solscan. Check token holdings for PBTC or SOSANA.

3. **Empty Network Wallets**: Search any of the "criminal network" addresses on Solscan and check their balance.

4. **DEX Pool**: Search `HLnpSz9h2S4hiLQ4mxtAYJJQXx9USzEXbte2RVP9QEd` on Solscan. Note it appears in virtually every CRM swap transaction.

5. **"Deleted" Wallets**: Search any closed wallet address on Solscan. Click "Transactions" to see the complete history still available.

---

## Note on Solana Account Closures

The investigation claimed that wallets being "deleted" (closed) represented evidence destruction. This is technically incorrect.

When a Solana token account is closed:
- The account's current state is removed from the active ledger
- The rent-exempt SOL deposit is reclaimed by the owner
- **Every transaction the account ever participated in remains permanently recorded**

You can query the complete history of any closed account using `getSignaturesForAddress` on any Solana RPC endpoint, or by searching the address on Solscan. Closing token accounts is routine user behaviour on Solana, commonly done to reclaim SOL from unused positions.

---

## Methodology

This counter-analysis uses exclusively:

- Solana mainnet RPC queries (`getBalance`, `getTokenAccountsByOwner`, `getAccountInfo`, `getSignaturesForAddress`)
- Helius API for enhanced transaction data (optional)
- On-chain token metadata (Metaplex)
- Public DEX and protocol documentation (Raydium, Jupiter)

No speculative analysis, pattern matching, or inference is used. Every claim can be independently verified.

---

## Disclaimer

This repository presents verifiable on-chain data and identified factual errors in a public investigation. It contains no editorial commentary. The author is a directly involved party (former technical contributor to the $CRM project) and has disclosed this throughout the accompanying documents.

This is not legal advice. Individuals who believe they have been harmed should consult with a qualified attorney.
