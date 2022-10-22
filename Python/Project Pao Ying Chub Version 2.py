
## Pao Ying Chub 2
pyc2 <- function() {
  pyc_values <- c("rock","scissors","paper")
  
  pyc_con <- c("rock : scissors", "scissors : paper", "paper : rock",
               "rock : rock", "scissors : scissors", "paper : paper",
               "rock : paper", "scissors : rock", "paper : scissors")

  pyc_con_result <- c("win",  "win",  "win",
                      "tie",  "tie",  "tie",
                      "lose", "lose", "lose")
  your_wins <- 0
  your_ties <- 0
  your_losses <- 0
  com_pyc <- " "
  your_pyc <- " "
  
  pyc_df <- data.frame(pyc_con,pyc_con_result)
             
  while (TRUE) {
  your_pyc <- readline("Your Choice : rock, scissors, paper, quit: ")
  if (your_pyc == "quit") {
    message(your_pyc)
    break
   } else {
      com_pyc <- sample(pyc_values,1)
      result_chk <- print(paste(your_pyc,":",com_pyc))
      result_output <- pyc_df[pyc_df$pyc_con == result_chk,2]
      if (length(result_output) == 0) {
        message ("You enter wrong condition")
        } else if (result_output == "win") {
          message ("You Win")
          your_wins = your_wins + 1
        } else if(result_output == "tie") {
          message ("You Tie")
          your_ties = your_ties + 1  
        } else if(result_output == "lose") {
          message ("You Lose")
          your_losses = your_losses + 1
        } else {}
    } 
  message(paste("wins =",your_wins," ties =",your_ties,"losses =",your_losses))
  }
} 
