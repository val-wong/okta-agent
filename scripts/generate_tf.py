import os
from pathlib import Path
import argparse

ZOOM_TF_TEMPLATE = """resource "okta_app_saml" "zoom" {{
  label                  = "Zoom SAML SCIM Demo"
  sso_url                = "{okta_sso_url}"
  recipient              = "https://zoom.us/saml/SSO"
  destination            = "https://zoom.us/saml/SSO"
  audience               = "https://zoom.us"
  subject_name_id_format = "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress"
  response_signed        = true
  signature_algorithm    = "RSA_SHA256"
  digest_algorithm       = "SHA256"

  attribute_statements {{
    type   = "EXPRESSION"
    name   = "Email"
    values = ["user.email"]
  }}

  attribute_statements {{
    type   = "EXPRESSION"
    name   = "FirstName"
    values = ["user.firstName"]
  }}

  attribute_statements {{
    type   = "EXPRESSION"
    name   = "LastName"
    values = ["user.lastName"]
  }}

  status = "ACTIVE"
}}

resource "okta_app_group_assignment" "zoom_assignment" {{
  app_id   = okta_app_saml.zoom.id
  group_id = "{group_id}"
}}
"""

def generate_zoom_tf(okta_sso_url, group_id):
    output_path = Path(__file__).resolve().parent.parent / "terraform" / "generated" / "zoom_saml.tf"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as f:
        f.write(ZOOM_TF_TEMPLATE.format(okta_sso_url=okta_sso_url, group_id=group_id))

    print(f"🧭 Absolute path: {output_path.resolve()}")
    print(f"✅ Terraform config written to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Zoom Terraform config.")
    parser.add_argument("--url", required=True, help="Okta SSO URL")
    parser.add_argument("--group", required=True, help="Okta Group ID")
    args = parser.parse_args()

    generate_zoom_tf(args.url, args.group)
