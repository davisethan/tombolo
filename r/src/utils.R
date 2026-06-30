named_matrix <- function(mat) {
  apply(mat, 1, function(row) as.list(row), simplify = FALSE)
}
