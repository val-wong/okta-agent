resource "okta_app_oauth" "poker_trivia_agent" {
  label                 = "Poker Trivia Agent"
  type                  = "web"
  grant_types           = ["authorization_code"]
  redirect_uris         = ["http://localhost:3000/callback"]
  response_types        = ["code"]
  client_uri            = "http://localhost:3000"
  logo_uri              = "https://via.placeholder.com/150"
}

resource "okta_app_oauth" "accounting_agent" {
  label                 = "Accounting Agent"
  type                  = "web"
  grant_types           = ["authorization_code"]
  redirect_uris         = ["http://localhost:3001/callback"]
  response_types        = ["code"]
  client_uri            = "http://localhost:3001"
  logo_uri              = "https://via.placeholder.com/150"
}
