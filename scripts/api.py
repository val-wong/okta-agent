# scripts/api.py

from fastapi import APIRouter, Query
import subprocess

router = APIRouter()

@router.get("/generate", tags=["Terraform"])
def generate_terraform(
    url: str = Query(..., description="Zoom SAML SSO URL"),
    group: str = Query(..., description="Okta Group ID for SCIM provisioning")
):
    """
    Run the generate_tf.py script with the provided SAML URL and Okta Group ID.
    """
    try:
        subprocess.run(
            ["python", "scripts/generate_tf.py", "--url", url, "--group", group],
            check=True
        )
        return {"status": "success", "message": "Terraform config generated successfully."}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}
