import argparse
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent

def run_scan():
    print("🔍 Running scan_okta_apps.py...")
    subprocess.run(["python", str(SCRIPT_DIR / "scan_okta_apps.py")], check=True)

def run_generate(url, group):
    print("🛠️ Generating Terraform config for Zoom...")
    subprocess.run([
        "python",
        str(SCRIPT_DIR / "generate_tf.py"),
        "--url", url,
        "--group", group
    ], check=True)

def generate_tf_config(url: str, group: str) -> str:
    result = subprocess.run(
        ["python", str(SCRIPT_DIR / "generate_tf.py"), "--url", url, "--group", group],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return result.stdout

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Okta SSO Automation CLI")
    parser.add_argument("--scan", action="store_true", help="Scan Okta apps for SAML/SCIM")
    parser.add_argument("--generate", action="store_true", help="Generate Terraform for Zoom SAML app")
    parser.add_argument("--url", help="Zoom SSO URL (required for generate)")
    parser.add_argument("--group", help="Okta Group ID (required for generate)")

    args = parser.parse_args()

    if args.scan:
        run_scan()
    elif args.generate:
        if not args.url or not args.group:
            parser.error("--generate requires --url and --group")
        run_generate(args.url, args.group)
    else:
        parser.print_help()
