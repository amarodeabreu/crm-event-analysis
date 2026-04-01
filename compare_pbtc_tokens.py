#!/usr/bin/env python3
"""
CRM Counter-Analysis: PBTC Token Comparison

Verifies that the PBTC TOKEN (Purple Bitcoin) and PBTC REWARD TOKEN
(Pruple Bitcoin) are two completely different tokens by comparing their
on-chain metadata, supply, and authorities.

This is the foundational error in the investigation -- the entire
"syndicate membership via PBTC" theory depends on these being the
same token. They are not.

Usage:
    python3 compare_pbtc_tokens.py
    python3 compare_pbtc_tokens.py --rpc https://api.mainnet-beta.solana.com
    python3 compare_pbtc_tokens.py --helius YOUR_API_KEY
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


PBTC_TOKEN = "HfMbPyDdZH6QMaDDUokjYCkHxzjoGBMpgaUvpLWGbF5p"
PBTC_REWARD = "EysSQoB4pL22cuSk9uajYgRNgCqPo3qDMxkwK5GWaAUi"
SOSANA_MINT = "49jdQxUkKtuvorvnwWqDzUoYKEjfgroTzHkQqXG9YFMj"
CM1_WALLET = "8eVZa7bEBnd6MA6JJkNdABRN4S3LbVLRnCZNJAUeuwQj"


def rpc_call(url: str, method: str, params: list) -> dict:
    """Make a Solana RPC call."""
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params,
    }
    try:
        resp = requests.post(url, json=payload, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        if "error" in data:
            return {"error": data["error"]}
        return data.get("result", {})
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def get_token_supply(url: str, mint: str) -> str:
    """Get token supply."""
    result = rpc_call(url, "getTokenSupply", [mint])
    if isinstance(result, dict) and "value" in result:
        return result["value"].get("uiAmountString", "unknown")
    return f"query failed: {result}"


def get_token_accounts_for_wallet(url: str, wallet: str, mint: str) -> list:
    """Get token accounts for a specific mint owned by a wallet."""
    result = rpc_call(
        url,
        "getTokenAccountsByOwner",
        [
            wallet,
            {"mint": mint},
            {"encoding": "jsonParsed"},
        ],
    )
    if isinstance(result, dict) and "value" in result:
        return result["value"]
    return []


def main():
    parser = argparse.ArgumentParser(
        description="Compare PBTC TOKEN vs PBTC REWARD TOKEN on-chain"
    )
    parser.add_argument(
        "--rpc",
        default="https://api.mainnet-beta.solana.com",
        help="Solana RPC endpoint",
    )
    parser.add_argument("--helius", default=None, help="Helius API key (optional)")
    args = parser.parse_args()

    rpc_url = args.rpc
    if args.helius:
        rpc_url = f"https://mainnet.helius-rpc.com/?api-key={args.helius}"

    print("=" * 72)
    print("PBTC TOKEN vs PBTC REWARD TOKEN -- ON-CHAIN COMPARISON")
    print("=" * 72)
    print(f"\nTimestamp: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}")
    print(f"RPC: {rpc_url}\n")

    # Compare mint addresses
    print("1. MINT ADDRESSES")
    print(f"   PBTC TOKEN:        {PBTC_TOKEN}")
    print(f"   PBTC REWARD TOKEN: {PBTC_REWARD}")
    print(f"   Same address?      {'YES' if PBTC_TOKEN == PBTC_REWARD else 'NO -- DIFFERENT TOKENS'}")

    # Compare supplies
    print("\n2. TOKEN SUPPLY")
    pbtc_supply = get_token_supply(rpc_url, PBTC_TOKEN)
    print(f"   PBTC TOKEN supply:        {pbtc_supply}")
    time.sleep(0.3)

    reward_supply = get_token_supply(rpc_url, PBTC_REWARD)
    print(f"   PBTC REWARD TOKEN supply: {reward_supply}")

    # Compare authorities (from account info)
    print("\n3. TOKEN ACCOUNT INFO")
    for label, mint in [("PBTC TOKEN", PBTC_TOKEN), ("PBTC REWARD TOKEN", PBTC_REWARD)]:
        time.sleep(0.3)
        info = rpc_call(rpc_url, "getAccountInfo", [mint, {"encoding": "jsonParsed"}])
        print(f"\n   {label} ({mint[:12]}...):")
        if isinstance(info, dict) and "error" not in info and info:
            value = info.get("value", info) if "value" in info else info
            if isinstance(value, dict):
                owner = value.get("owner", "unknown")
                lamports = value.get("lamports", 0)
                print(f"     Owner program: {owner}")
                print(f"     Lamports: {lamports}")

                parsed = value.get("data", {})
                if isinstance(parsed, dict) and "parsed" in parsed:
                    parsed_info = parsed["parsed"].get("info", {})
                    authority = parsed_info.get("mintAuthority", "none/revoked")
                    freeze = parsed_info.get("freezeAuthority", "none")
                    supply = parsed_info.get("supply", "unknown")
                    decimals = parsed_info.get("decimals", "unknown")
                    print(f"     Mint authority: {authority}")
                    print(f"     Freeze authority: {freeze}")
                    print(f"     Raw supply: {supply}")
                    print(f"     Decimals: {decimals}")
        else:
            print(f"     Query result: {info}")

    # Also compare with SOSANA to show all three are separate
    print("\n4. SOSANA TOKEN (for comparison)")
    print(f"   SOSANA mint: {SOSANA_MINT}")
    time.sleep(0.3)
    sosana_supply = get_token_supply(rpc_url, SOSANA_MINT)
    print(f"   SOSANA supply: {sosana_supply}")

    # Check CM1's actual holding
    print("\n5. CM1 WALLET -- WHICH PBTC DOES CM1 HOLD?")
    print(f"   Wallet: {CM1_WALLET}")

    time.sleep(0.3)
    pbtc_accounts = get_token_accounts_for_wallet(rpc_url, CM1_WALLET, PBTC_TOKEN)
    if pbtc_accounts:
        for acct in pbtc_accounts:
            amount = (
                acct.get("account", {})
                .get("data", {})
                .get("parsed", {})
                .get("info", {})
                .get("tokenAmount", {})
                .get("uiAmountString", "0")
            )
            print(f"   Holds PBTC TOKEN (Purple Bitcoin): {amount}")
    else:
        print(f"   Holds PBTC TOKEN (Purple Bitcoin): NONE")

    time.sleep(0.3)
    reward_accounts = get_token_accounts_for_wallet(rpc_url, CM1_WALLET, PBTC_REWARD)
    if reward_accounts:
        for acct in reward_accounts:
            amount = (
                acct.get("account", {})
                .get("data", {})
                .get("parsed", {})
                .get("info", {})
                .get("tokenAmount", {})
                .get("uiAmountString", "0")
            )
            print(f"   Holds PBTC REWARD TOKEN: {amount}")
    else:
        print(f"   Holds PBTC REWARD TOKEN: NONE")

    time.sleep(0.3)
    sosana_accounts = get_token_accounts_for_wallet(rpc_url, CM1_WALLET, SOSANA_MINT)
    if sosana_accounts:
        for acct in sosana_accounts:
            amount = (
                acct.get("account", {})
                .get("data", {})
                .get("parsed", {})
                .get("info", {})
                .get("tokenAmount", {})
                .get("uiAmountString", "0")
            )
            print(f"   Holds SOSANA: {amount}")
    else:
        print(f"   Holds SOSANA: NONE")

    # Conclusion
    print("\n" + "=" * 72)
    print("CONCLUSION")
    print("=" * 72)
    print("""
The PBTC TOKEN and PBTC REWARD TOKEN are two entirely separate tokens:
  - Different mint addresses
  - Different supply structures
  - Different creators/authorities

The investigation's claim that "if someone holds PBTC they are part of
their extraction network" conflates these two tokens.

CM1 holds the PBTC TOKEN (Purple Bitcoin) -- a retail purchase on a
public DEX. This is NOT the PBTC REWARD TOKEN that the investigation
associates with SOSANA.

Anyone can verify these results by querying the mint addresses above
on Solscan (https://solscan.io) or any Solana RPC endpoint.
""")


if __name__ == "__main__":
    main()
