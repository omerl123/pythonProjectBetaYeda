def logs(T, A , S, Email ):
    # Receives a string and a double and puts it in a text file
    if (S==1):
        with open('BetaLogs.txt', 'a') as f:
            f.write("step: " + str(S) + " The Login success to email:" + Email + "\n" + "The time it took to " + A + ":" + str(T) + " seconds.\n")
    elif (S==2):
        with open('BetaLogs.txt', 'a') as f:
            f.write("step: " + str(S) + " move to " + A + " It took, " + str(T) + " seconds.\n")
    else:
        with open('BetaLogs.txt', 'a') as f:
            f.write("step: " + str(S) + " complete " + A + " ,until this stage completed :" + str(round(T * 100)) +"% from this skill.\n")

def Fail(Email):
    with open('BetaLogs.txt', 'a') as f:
        f.write("The Login to " + Email + " Fail. \n")

def CalcStep(Email, minuts, seconds, total):
    with open('BetaLogs.txt', 'a') as f:
        f.write(Email + " complete the skill. \n" + "total time the script run: " + str(minuts) + " minuts " + "and " + str(seconds) + " second\n"
                           "the test complete " + str(total * 100) + "%\n")