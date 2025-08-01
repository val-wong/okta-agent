variable "okta_org_name" {
  description = "https://integrator-1067802.okta.com/"
  type        = string
}

variable "okta_api_token" {
  description = "API token for Okta environment"
  type        = string
  sensitive   = true
}
