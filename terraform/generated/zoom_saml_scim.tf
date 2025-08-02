resource "okta_app_saml" "zoom" {
  label                  = "Zoom SAML SCIM Demo"
  recipient              = "https://zoom.us/saml/SSO"
  destination            = "https://zoom.us/saml/SSO"
  audience               = "https://zoom.us"
  subject_name_id_format = "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress"
  response_signed        = true
  signature_algorithm    = "RSA_SHA256"
  digest_algorithm       = "SHA256"

  attribute_statements {
    type   = "EXPRESSION"
    name   = "Email"
    values = ["user.email"]
  }

  attribute_statements {
    type   = "EXPRESSION"
    name   = "FirstName"
    values = ["user.firstName"]
  }

  attribute_statements {
    type   = "EXPRESSION"
    name   = "LastName"
    values = ["user.lastName"]
  }

  status = "ACTIVE"
}

resource "okta_app_group_assignment" "zoom_assignment" {
  app_id   = okta_app_saml.zoom.id
  group_id = "00gabcxyz00gtoai5ejN40FQlH697" 
}
