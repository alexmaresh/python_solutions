# Given the participants' scoresheet for your University Sports Day, you are required to find the runner-up score.
# You are given  scores. Store them in a list and find the score of the runner-up.
# Given list is [2,3,4,5,5,6]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.


def runner_up_score(arr: list):
    x = list(set(arr))
    x.sort()
    return x[-2]
