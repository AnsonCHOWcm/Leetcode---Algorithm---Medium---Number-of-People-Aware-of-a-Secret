class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        people_who_know_secret = 1
        people_who_can_share_secret = 0
        people_who_know_secret_by_day = [1]

        for day in range(1, n + 1):

            curr_people_who_forgot_secret = 0
            curr_people_who_can_share_secret = 0

            if day > forget:
                curr_people_who_forgot_secret = people_who_know_secret_by_day[day - forget]

            if day > delay:
                curr_people_who_can_share_secret = people_who_know_secret_by_day[day - delay]

            people_who_can_share_secret = people_who_can_share_secret - curr_people_who_forgot_secret + curr_people_who_can_share_secret

            if day == 1:
                people_who_know_secret_by_day.append(1)
            else:
                people_who_know_secret_by_day.append(people_who_can_share_secret)

            people_who_know_secret = people_who_know_secret - curr_people_who_forgot_secret + people_who_can_share_secret

        return people_who_know_secret % (pow(10, 9) + 7)