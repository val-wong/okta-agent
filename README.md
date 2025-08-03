## 🛡️ Okta Terraform Agent

This project is a Python-based CLI tool that automates scanning your Okta apps and generating Terraform configuration for SSO (SAML) and SCIM provisioning. Ideal for DevOps engineers, IT admins, or platform teams managing Identity at scale.

---

### 📁 Project Structure

```
okta-sso-agent/
├── terraform/
├── scripts/
│   ├── agent.py         ← CLI entry point
│   ├── scan_okta_apps.py
│   └── generate_tf.py
├── .env
├── .github/workflows/ci.yml ← GitHub Actions CI/CD pipeline
└── README.md
```

---

### 🚀 Features

* 🔍 Scan Okta apps via API
* 🛠️ Generate SAML + SCIM Terraform blocks
* 🧹 Modular Python CLI (`argparse`)
* ⚙️ GitHub Actions CI/CD pipeline
* 🔐 Environment variable support (`.env`)

---

### 🧪 Usage

```bash
# Scan your Okta org
python scripts/agent.py --scan

# Generate Terraform config for Zoom
python scripts/agent.py --generate \
  --url "https://your-okta-domain.com/app/zoom/sso/saml" \
  --group "your-group-id"
```

---

### 🔐 Environment Setup

Create a `.env` file in the project root:

```
OKTA_DOMAIN=https://your-okta-domain.okta.com
OKTA_API_TOKEN=your_api_token_here
```

---

### 🧱 CI/CD

Your pipeline runs:

* `flake8` linting
* `pytest` (if tests are added later)
* CI on push to `main`

---

### 📺 Related Videos

* 🎥 [Part 1: Scanning + Terraform Generator](#)
* 🎥 [Part 2: Building the CLI Agent](#)
* 🎥 [Part 3: CI/CD with GitHub Actions](#)

---

### 🤝 Contributing

Feel free to fork and PR improvements, especially:

* Support for more apps
* SCIM provisioning config generation
* Multi-env support

---

### 🔗 Connect

Made by [Valentin Wong](https://www.linkedin.com/in/valentinwong/)
