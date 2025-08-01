terraform {
  required_providers {
    okta = {
      source  = "okta/okta"
      version = "~> 4.0"
    }
  }
}

provider "okta" {
  org_name  = var.okta_org_name
  base_url  = "okta.com"
  api_token = var.okta_api_token
}

resource "okta_app_oauth" "example_app" {
  label                 = "Poker Trivia Agent"
  type                  = "web"
  grant_types           = ["authorization_code"]
  redirect_uris         = ["http://localhost:3000/callback"]
  response_types        = ["code"]
  client_uri            = "http://localhost:3000"
  logo_uri              = "https://via.placeholder.com/150"
}

resource "okta_app_oauth" "example_app_1" {
  label                 = "Accounting Agent"
  type                  = "web"
  grant_types           = ["authorization_code"]
  redirect_uris         = ["http://localhost:3001/callback"]
  response_types        = ["code"]
  client_uri            = "http://localhost:3001"
  logo_uri              = "https://via.placeholder.com/150"
}
