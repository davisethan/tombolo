library(jsonlite)

send <- function(id, result) {
  cat(toJSON(list(jsonrpc = "2.0", id = id, result = result),
    auto_unbox = TRUE, na = "null"
  ))
}

send_error <- function(id, code, message) {
  cat(toJSON(list(jsonrpc = "2.0", id = id, error = list(code = code, message = message)),
    auto_unbox = TRUE, na = "null"
  ))
  quit(save = "no", status = 0)
}
