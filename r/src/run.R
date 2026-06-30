source("rpc.R")
source("nma.R")
source("bnma.R")

handlers <- list(nma = nma, bnma = bnma)

req <- tryCatch(
  fromJSON(readLines(file("stdin"), warn = FALSE)),
  error = function(e) send_error(NULL, -32700L, "Parse error")
)

if (is.null(req$method) || is.null(req$params)) {
  send_error(req$id, -32600L, "Invalid Request")
}

if (!(req$method %in% names(handlers))) {
  send_error(req$id, -32601L, paste("Method not found:", req$method))
}

if (is.null(req$params$data) || is.null(req$params$greater_is_better)) {
  send_error(req$id, -32602L, "Invalid params")
}

result <- tryCatch(
  handlers[[req$method]](req$params$data, req$params$greater_is_better),
  error = function(e) send_error(req$id, -32603L, conditionMessage(e))
)

send(req$id, result)
