## Pao Ying Chub 1
pyc1 <- function() {
  pyc_choices <- c("rock", "scissors", "paper")
  your_wins <- 0
  your_ties <- 0
  your_losses <- 0

    while (TRUE) { 
    my_pyc <- readline("Your Choice:rock,scissors,paper,quit: ")

      if ( my_pyc == "quit" ) {
          message(my_pyc) 
          break
      } else {
          com_pyc <- sample(pyc_choices,1)
          message(paste(my_pyc,":",com_pyc))
          if (my_pyc == "rock" & com_pyc == "rock") {
              message("you tie")
              your_ties <- your_ties+1
            } else if (my_pyc == "rock" & com_pyc == "scissors") {
              message("you win")
              your_wins <- your_wins+1
            } else if (my_pyc == "rock" & com_pyc == "paper") {
              message("you lose")
              your_losses <- your_losses+1
            } else if (my_pyc == "scissors" & com_pyc == "rock") {
              message("you lose")
              your_losses <- your_losses+1
            } else if (my_pyc == "scissors" & com_pyc == "scissors") {
              message("you tie")
              your_ties <- your_ties+1
            } else if (my_pyc == "scissors" & com_pyc == "paper") {
              message("you win")
              your_wins <- your_wins+1
            } else if (my_pyc == "paper" & com_pyc == "rock") {
              message("you win")
              your_wins <- your_wins+1
            } else if (my_pyc == "paper" & com_pyc == "scissors") {
              message("you lose")
              your_losses <- your_losses+1
            } else if (my_pyc == "paper" & com_pyc == "paper") {
              message("you tie")
              your_ties <- your_ties+1
          } else {
              message("You enter wrong condition")
##              result_pyc <- glue("{my_pyc}:{com_pyc}")
##              print(result_pyc)
          }
          message(paste("wins=",your_wins,",ties=",your_ties,",losses=",your_losses))
      }
    }
}
