#!/usr/bin/env python3
"""
CRM Counter-Analysis: Wallet Transaction History

Retrieves the complete transaction history for any Solana wallet address.
Useful for verifying whether "empty" wallets ever held the assets claimed
in the investigation, or whether "deleted" wallets have recoverable history.

Usage:
    python3 wallet_history.py ADDRESS
    python3 wallet_history.py ADDRESS --limit 100
    python3 wallet_history.py ADDRESS --helius YOUR_API_KEY
    python3 wallet_history.py ADDRESS --output history.json

On Solana, closing a token account does NOT delete transaction history.
Every transaction is permanent and publicly queryable regardless of
whether the account is currently open or closed.
"""

import argparse
import json
import sys
import time

try:
    import requests
except ImportError:
    print("ERROR: 'requests' library required. Install with: pip install requests")
    sys.exit(1)


def get_signatures(rpc_url: str, address: str, limit: int = 1000) -> list:
    """Fetch transaction signatures for an address, paginating if needed."""
    all_sigs = []
    before = None
    batch_size = min(limit, 1000)
    remaining = limit

    while remaining > 0:
        params = [address, {"limit": min(batch_size, remaining)}]
        if before:
            params[1]["before"] = before

        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getSignaturesForAddress",
            "params": params,
        }

        try:
            resp = requests.post(rpc_url, json=payload, timeout=30)
            resp.raise_for_status()
            data = resp.json()
        except requests.exceptions.RequestException as e:
            print(f"ERROR: RPC request failed: {e}")
            break

        if "error" in data:
            print(f"ERROR: {data['error']}")
            break

        result = data.get("result", [])
        if not result:
            break

        all_sigs.extend(result)
        remaining -= len(result)
        before = result[-1]["signature"]

        if len(result) < batch_size:
            break

        time.sleep(0.2)  # Rate limit protection

    return all_sigs


def main():
    parser = argparse.ArgumentParser(
        description="Retrieve complete transaction history for a Solana wallet"
    )
    parser.add_argument("address", help="Solana wallet address to investigate")
    parser.add_argument(
        "--limit",
        type=int,
        default=100,
        help="Maximum number of transactions to retrieve (default: 100)",
    )
    parser.add_argument(
        "--rpc",
        default="https://api.mainnet-beta.solana.com",
        help="Solana RPC endpoint",
    )
    parser.add_argument("--helius", default=None, help="Helius API key (optional)")
    parser.add_argument(
        "--output", default=None, help="Save full results to JSON file"
    )
    args = parser.parse_args()

    rpc_url = args.rpc
    if args.helius:
        rpc_url = f"https://mainnet.helius-rpc.com/?api-key={args.helius}"

    print(f"Wallet: {args.address}")
    print(f"RPC: {rpc_url}")
    print(f"Fetching up to {args.limit} transactions...\n")

    signatures = get_signatures(rpc_url, args.address, args.limit)

    if not signatures:
        print("NO TRANSACTIONS FOUND.")
        print(
            "\nThis means either:\n"
            "  1. The address has never transacted on Solana mainnet, OR\n"
            "  2. The RPC endpoint is rate-limited (try with --helius key)\n"
        )
        return

    print(f"Found {len(signatures)} transactions.\n")
    print(f"{'#':<5} {'Slot':<12} {'Time':<22} {'Status':<8} {'Signature'}")
    print("-" * 100)

    for i, sig in enumerate(signatures):
        slot = sig.get("slot", "?")
        block_time = sig.get("blockTime")
        if block_time:
            time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(block_time))
        else:
            time_str = "unknown"
        err = sig.get("err")
        status = "OK" if err is None else "FAILED"
        signature = sig.get("signature", "?")

        print(f"{i+1:<5} {slot:<12} {time_str:<22} {status:<8} {signature[:40]}...")

    # Summary stats
    if signatures:
        first_time = signatures[-1].get("blockTime")
        last_time = signatures[0].get("blockTime")

        print(f"\n--- Summary ---")
        print(f"Total transactions retrieved: {len(signatures)}")
        if first_time:
            print(
                f"Earliest transaction: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime(first_time))}"
            )
        if last_time:
            print(
                f"Latest transaction:   {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime(last_time))}"
            )

        failed = sum(1 for s in signatures if s.get("err") is not None)
        print(f"Successful: {len(signatures) - failed}")
        print(f"Failed: {failed}")

    # Optionally save to JSON
    if args.output:
        with open(args.output, "w") as f:
            json.dump(
                {
                    "address": args.address,
                    "query_time": time.strftime(
                        "%Y-%m-%d %H:%M:%S UTC", time.gmtime()
                    ),
                    "total_transactions": len(signatures),
                    "signatures": signatures,
                },
                f,
                indent=2,
            )
        print(f"\nFull results saved to: {args.output}")

    print(
        f"\nView any transaction on Solscan:"
        f"\n  https://solscan.io/tx/SIGNATURE_HERE"
    )
    print(
        f"\nView this wallet on Solscan:"
        f"\n  https://solscan.io/account/{args.address}"
    )


if __name__ == "__main__":
    main()
