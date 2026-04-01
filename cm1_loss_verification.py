#!/usr/bin/env python3
"""
CM1 Loss Verification: Historical CRM Holdings Analysis

Uses Helius Enhanced Transaction API to pull all CRM token transfers
across CM1's 17 voluntarily disclosed wallets, reconstruct buy/sell
history, and calculate total investment vs proceeds.

Usage:
    python3 cm1_loss_verification.py
    python3 cm1_loss_verification.py --output cm1_loss_results.json
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone

try:
    import requests
except ImportError:
    print("ERROR: 'requests' library required. Install with: pip install requests")
    sys.exit(1)


HELIUS_API_KEY = os.environ.get("HELIUS_API_KEY", "")
HELIUS_TX_URL = "https://api-mainnet.helius-rpc.com/v0/addresses/{address}/transactions/"
HELIUS_RPC_URL = f"https://mainnet.helius-rpc.com/?api-key={HELIUS_API_KEY}"

CRM_MINT = "Eme5T2s2HB7B8W4YgLG1eReQpnadEVUnQBRjaKTdBAGS"

CM1_WALLETS = {
    "Main Wallet": "8eVZa7bEBnd6MA6JJkNdABRN4S3LbVLRnCZNJAUeuwQj",
    "Cluster #2": "8pyiqMctEzfUZvegKH5jHenHTBkQ5W37WSAitieYZz3m",
    "Cluster #3": "3be81bNMaqNbQeD8Lp1aTRdQWigx3fSbXv9VNwWkFYNU",
    "Cluster #4": "J3V68JvjXFArRBb86NAX8mCoYgFce7MmZjs9ziz74RzT",
    "Cluster #5": "44K8GNKraJi5SkPWrhXSsRKnHwMLKwrXTnpQpPxVt1Vp",
    "Cluster #6": "2pT6gSDvY7RvNeE3YpCdBJKr8VV3tStsAAvYzuuVESGG",
    "Cluster #7": "3Vv5jty3PQqpufoLQFb7aq512YNRBwJLZLWJsB5wxqjY",
    "Separate #1": "6pCjijfb14dJf4HbLULXXVZc7DjFyWYC134opbaUygTX",
    "Separate #2": "92wvRxnPKbPa12Wy12jEUUV2hgkvrXXxCubRuLkQjS5e",
    "Separate #3": "5V4RVd9NeZdzWicwmKPxn6cqZyj4KPmnWsSR7Qt4BaEG",
    "Separate #4": "8EWS9VME69oBvsbi395uHaryx9vuZN4wmxwubmdNCPHM",
    "Separate #5": "5HAjsEM1sxXLPZHTQTnJxL32eJdxCaj27cXddN7BVQyG",
    "Separate #6": "PrXXTmzWuYNrrVGhueGYeEHufTfR96udW4yp3VnX185",
    "Separate #7": "997vQdnJrNspvJPU8rvFtbkRuoJgFrKeN3zxcAnwn2s8",
    "Separate #8": "CyhJT3o8xrW5vvenMkrJDdpYcdboGGg6SQvSoeVtcA35",
    "Separate #9": "69DNYgQLUBavWr7hmrHUBZoAVaZgnFQgxHVKtsULuf8A",
    "Separate #10": "HvaTTY5h4mC76inmNc9N8KsYwEgaqyXJ91qd2yh8GnPH",
}

AMARO_WALLETS = {
    "Amaro Wallet #1": "8sPr8iXWB3qWCC7V82ffYydtqoNjqwHZq4TM4VfVzFBf",
    "Amaro Wallet #2": "7abBmGf4HNu3UXsanJc7WwAPW2PgkEb9hwrFKwCySvyL",
    "Amaro Wallet #3": "HCw8hKqSahdjY2y7UNubUyMBd521ZJUxB2Eg1VnbSz3W",
}

CM2_WALLETS = {
    "CM2 Coinbase": "GEiTi7Qf6gZT4QinNbm29o7Skstb5jTRgB1C8y1io4MR",
    "CM2 Axiom #1": "E9bg6VCatYJGgrjADYbGdRF43HC3nqsFdqnQNk54oPpV",
    "CM2 Axiom #2": "EQGuHysoEdjnk7sst8WqK8BZEmju8VhUf52xmmueYTUa",
    "CM2 Axiom #3": "2cymcQGQz3fnTwW5FLQC8afDFm2yhC8h4kpUud1QB7Gf",
    "CM2 Axiom #4": "BKLBtcJQJ2MxJP6wfbRkoqrYNWUPVLfeB8vs91agBxjt",
    "CM2 Axiom #5": "5Mi553gMwXHFw2nAKxNt7WWDvoLYr5aAE3xMDHELMzan",
    "CM2 BullX": "CTjSDRDnTRu4634fHEUU9C6KmtYy3hwNr9Xc6atkEnqC",
    "CM2 Phantom #1": "Hqofe3acFetVfYx9iEcLD8jTeT8LTpfQo9exxPjbvG6j",
    "CM2 Phantom #2": "CS4UYi21ummGDZM4nGirGEpZyafQudoN1Cg7ub7k3PSY",
    "CM2 Phantom #3": "bjRAqsuvF8qRsAm4vZCo63BRMV6vkbs78pWAsMMPHBV",
    "CM2 Phantom #4": "G8HJH3V9Fkq63ASof69b9BhAM9iSpdtHTuEfXLgKVZJp",
    "CM2 Phantom #5": "EFZbvJa67GqJudEjHGSQgr8S17NnQG3umzGWxJjxgzF2",
    "CM2 Phantom #6": "8KrPgiPpwY4fLvWiwsDGy9uZvmJmdzyiqwVedn3XDzdn",
    "CM2 Phantom #7": "XSP6hhxWLH8x6MZzHbsvV7qGchmAg34mX8kUccrcfbw",
    "CM2 Phantom #8": "EQaDzZsejHemqFVWEEnPLWv5s5P5VdQG5UkhCn69EvkN",
    "CM2 Phantom #9": "GDJQSuShLnn9kFuHBfg8GfkSHNKpVMTaYo1dAzCdjgeS",
    "CM2 Phantom #10": "3aw6ETxXNUtTp9ZpfY8MRWmCGbbYUZ3efoih1f8JQKmu",
    "CM2 Phantom #11": "6J1R2YygZoTDF5qeFhuUAWtjqGVTpLte5VMKtST7HhXz",
    "CM2 Phantom #12": "6WoBvj3Fq91UKeb85M2wP7Jc3HH5f7rG2F24KbDi38Dm",
    "CM2 Phantom #13": "2wms1Voxam4gJvZcNsgk6MKNAw78cxdtU4pACFgsUXiT",
    "CM2 Phantom #14": "G4r8rSpvKvYa3ELGuic68DHWSEczTEq1VgiGnCVJJyin",
    "CM2 Phantom #15": "EwhA5bnPApWjwbYJRw3rrj2CpC6gZPJm3AcbV6LsRXqW",
    "CM2 Phantom #16": "45abtM4LVpQMvBpVENAhFGZWNKugLv6gKAZKKJif14Ua",
}

# All wallets combined for total loss calculation
ALL_WALLETS = {**CM1_WALLETS, **AMARO_WALLETS, **CM2_WALLETS}


def get_all_transactions(wallet_addr, max_pages=20):
    """Fetch all transactions for a wallet using Helius enhanced API with pagination."""
    all_txs = []
    last_sig = None

    for page in range(max_pages):
        url = HELIUS_TX_URL.format(address=wallet_addr)
        params = {"api-key": HELIUS_API_KEY, "limit": 100}
        if last_sig:
            params["before"] = last_sig

        for attempt in range(5):
            try:
                resp = requests.get(url, params=params, timeout=30)
                if resp.status_code == 429:
                    wait = 2 ** (attempt + 1)
                    print(f"    Rate limited, waiting {wait}s...")
                    time.sleep(wait)
                    continue
                resp.raise_for_status()
                data = resp.json()
                break
            except requests.exceptions.RequestException as e:
                if attempt < 4:
                    time.sleep(2)
                    continue
                print(f"    ERROR: {e}")
                return all_txs
        else:
            return all_txs

        if not isinstance(data, list) or len(data) == 0:
            break

        all_txs.extend(data)
        last_sig = data[-1].get("signature")

        if len(data) < 100:
            break

        time.sleep(0.3)

    return all_txs


def extract_crm_transfers(txs, wallet_addr):
    """Extract all CRM token transfers from Helius parsed transactions."""
    crm_transfers = []

    for tx in txs:
        if tx.get("transactionError"):
            continue

        token_transfers = tx.get("tokenTransfers", [])
        native_transfers = tx.get("nativeTransfers", [])

        for tt in token_transfers:
            if tt.get("mint") != CRM_MINT:
                continue

            amount = tt.get("tokenAmount", 0)
            from_addr = tt.get("fromUserAccount", "")
            to_addr = tt.get("toUserAccount", "")

            if from_addr == wallet_addr:
                direction = "out"
                counterparty = to_addr
            elif to_addr == wallet_addr:
                direction = "in"
                counterparty = from_addr
            else:
                continue

            # Calculate SOL change for the wallet in same tx (native transfers only)
            # Note: DEX aggregators (OKX, Jupiter) may route proceeds through
            # wrapped SOL (wSOL), which won't appear in native transfers.
            sol_change = 0.0
            for nt in native_transfers:
                if nt.get("fromUserAccount") == wallet_addr:
                    sol_change -= nt.get("amount", 0) / 1e9
                if nt.get("toUserAccount") == wallet_addr:
                    sol_change += nt.get("amount", 0) / 1e9

            timestamp = tx.get("timestamp", 0)
            dt = datetime.fromtimestamp(timestamp, tz=timezone.utc) if timestamp else None

            crm_transfers.append({
                "signature": tx.get("signature", ""),
                "timestamp": dt.strftime("%Y-%m-%d %H:%M UTC") if dt else "unknown",
                "epoch": timestamp,
                "type": tx.get("type", "UNKNOWN"),
                "source": tx.get("source", "UNKNOWN"),
                "direction": direction,
                "amount": amount,
                "sol_change": sol_change,
                "counterparty": counterparty,
                "description": tx.get("description", ""),
            })

    return crm_transfers


def main():
    parser = argparse.ArgumentParser(description="CM1 CRM Loss Verification")
    parser.add_argument("--helius", default=None, help="Helius API key (or set HELIUS_API_KEY env var)")
    parser.add_argument("--output", default=None, help="Save results to JSON file")
    args = parser.parse_args()

    global HELIUS_API_KEY, HELIUS_RPC_URL
    if args.helius:
        HELIUS_API_KEY = args.helius
        HELIUS_RPC_URL = f"https://mainnet.helius-rpc.com/?api-key={HELIUS_API_KEY}"
    if not HELIUS_API_KEY:
        print("ERROR: Helius API key required. Set HELIUS_API_KEY env var or pass --helius KEY")
        sys.exit(1)

    print("=" * 72)
    print("COMBINED LOSS VERIFICATION: CM1 + AMARO + CM2 HISTORICAL CRM ANALYSIS")
    print("=" * 72)
    print(f"CRM Mint: {CRM_MINT}")
    print(f"CM1 wallets: {len(CM1_WALLETS)}")
    print(f"Amaro wallets: {len(AMARO_WALLETS)}")
    print(f"CM2 wallets: {len(CM2_WALLETS)}")
    print(f"Total wallets: {len(ALL_WALLETS)}")
    print(f"API: Helius Enhanced Transaction API")
    print()

    all_results = {}
    grand_total_in = 0.0
    grand_total_out = 0.0
    grand_total_sol_spent = 0.0
    grand_total_sol_received = 0.0
    total_crm_txs = 0
    all_crm_events = []

    for label, wallet in ALL_WALLETS.items():
        print(f"\n{'─' * 60}")
        print(f"  {label}: {wallet}")
        print(f"{'─' * 60}")

        txs = get_all_transactions(wallet)
        print(f"  Total transactions fetched: {len(txs)}")

        crm_transfers = extract_crm_transfers(txs, wallet)
        print(f"  CRM token transfers: {len(crm_transfers)}")

        wallet_in = 0.0
        wallet_out = 0.0
        wallet_sol_spent = 0.0
        wallet_sol_received = 0.0

        for t in sorted(crm_transfers, key=lambda x: x.get("epoch", 0)):
            direction_label = "BUY " if t["direction"] == "in" else "SELL"
            sol_label = ""
            if t["sol_change"] != 0:
                sol_label = f" (SOL: {t['sol_change']:+.4f})"

            print(f"    {t['timestamp']} | {direction_label} {t['amount']:>15,.2f} CRM{sol_label}  [{t['source']}]")

            if t["direction"] == "in":
                wallet_in += t["amount"]
                if t["sol_change"] < 0:
                    wallet_sol_spent += abs(t["sol_change"])
            else:
                wallet_out += t["amount"]
                if t["sol_change"] > 0:
                    wallet_sol_received += t["sol_change"]

            t["wallet_label"] = label
            t["wallet_address"] = wallet
            all_crm_events.append(t)

        total_crm_txs += len(crm_transfers)
        grand_total_in += wallet_in
        grand_total_out += wallet_out
        grand_total_sol_spent += wallet_sol_spent
        grand_total_sol_received += wallet_sol_received

        if crm_transfers:
            print(f"\n    Wallet subtotals:")
            print(f"      CRM acquired: {wallet_in:>15,.2f}")
            print(f"      CRM disposed: {wallet_out:>15,.2f}")
            print(f"      SOL spent buying CRM:    {wallet_sol_spent:>10.4f}")
            print(f"      SOL received selling CRM: {wallet_sol_received:>10.4f}")

        all_results[label] = {
            "address": wallet,
            "total_transactions": len(txs),
            "crm_transactions": len(crm_transfers),
            "crm_in": wallet_in,
            "crm_out": wallet_out,
            "sol_spent": wallet_sol_spent,
            "sol_received": wallet_sol_received,
            "transfers": crm_transfers,
        }

        time.sleep(0.5)

    # Sort all CRM events chronologically
    all_crm_events.sort(key=lambda x: x.get("epoch", 0))

    # Summary
    print("\n" + "=" * 72)
    wallet_count = len(ALL_WALLETS)
    print(f"AGGREGATE SUMMARY ACROSS ALL {wallet_count} WALLETS (17 CM1 + 3 AMARO + 23 CM2)")
    print("=" * 72)
    print(f"  Total CRM transfers found:      {total_crm_txs}")
    print(f"  Total CRM acquired (buys/in):   {grand_total_in:>15,.2f}")
    print(f"  Total CRM disposed (sells/out): {grand_total_out:>15,.2f}")
    print(f"  Net CRM position:               {grand_total_in - grand_total_out:>15,.2f}")
    print(f"  Total SOL spent on CRM:         {grand_total_sol_spent:>10.4f} SOL")
    print(f"  Total SOL received from CRM:    {grand_total_sol_received:>10.4f} SOL")
    net_sol = grand_total_sol_received - grand_total_sol_spent
    print(f"  Net SOL (received - spent):     {net_sol:>10.4f} SOL")
    print()
    print("  NOTE: Some DEX sell proceeds (OKX, Jupiter) route through wrapped")
    print("  SOL (wSOL) and may not appear in native SOL transfer totals above.")
    print("  Actual SOL received from sells may be higher than reported.")
    print()

    # Estimate USD loss if we have SOL figures
    if grand_total_sol_spent > 0 or grand_total_sol_received > 0:
        print("  USD LOSS ESTIMATE:")
        print("  (Using approximate SOL prices at time of transactions)")
        for sol_price in [130, 135, 140]:
            usd_spent = grand_total_sol_spent * sol_price
            usd_received = grand_total_sol_received * sol_price
            usd_loss = usd_spent - usd_received
            print(f"    At SOL=${sol_price}: spent ${usd_spent:,.2f}, received ${usd_received:,.2f}, net loss: ${usd_loss:,.2f}")
        print()

    print("  WALLET RELATIONSHIPS:")
    print("    CM1_WALLET    -> Amaro Wallet #2 (30,000,000 CRM, Dec 31 2025: 1M+9M+10M+10M)")
    print("    CM1_CLUSTER_6 -> Amaro Wallet #1 (10,000,000 CRM, Feb 28 2026)")
    print("    Amaro Wallet #2 -> intermediary -> Amaro Wallet #1 (10,000,000 CRM, Mar 1 2026)")
    print("    Amaro Wallet #3 acquired CRM via OKX DEX (2,044,480 CRM, Feb 13 2026)")
    print("    CM2: 23 wallets, all Coinbase-funded (1 Coinbase + 5 Axiom + 1 BullX + 16 Phantom)")
    print()
    print(f"  CM1 + Amaro combined self-reported loss: $70,000-$80,000")
    print(f"  CM2 losses: documented separately")
    print(f"  Current CRM holdings across all {wallet_count} wallets: 0 CRM")

    # Timeline of CRM events
    if all_crm_events:
        print(f"\n{'=' * 72}")
        print("CHRONOLOGICAL CRM TRANSACTION TIMELINE (ALL WALLETS)")
        print(f"{'=' * 72}")
        for evt in all_crm_events:
            d = "BUY " if evt["direction"] == "in" else "SELL"
            sol = f" SOL:{evt['sol_change']:+.4f}" if evt["sol_change"] != 0 else ""
            print(f"  {evt['timestamp']} | {evt['wallet_label']:15s} | {d} {evt['amount']:>12,.2f} CRM{sol}")

    if args.output:
        output = {
            "generated": datetime.now(timezone.utc).isoformat(),
            "crm_mint": CRM_MINT,
            "wallets_checked": len(ALL_WALLETS),
            "total_crm_transactions": total_crm_txs,
            "aggregate": {
                "total_crm_in": grand_total_in,
                "total_crm_out": grand_total_out,
                "net_crm": grand_total_in - grand_total_out,
                "total_sol_spent": grand_total_sol_spent,
                "total_sol_received": grand_total_sol_received,
                "net_sol": net_sol,
            },
            "timeline": all_crm_events,
            "wallets": all_results,
        }
        with open(args.output, "w") as f:
            json.dump(output, f, indent=2, default=str)
        print(f"\n  Results saved to: {args.output}")


if __name__ == "__main__":
    main()
