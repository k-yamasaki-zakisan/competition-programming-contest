class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        now_person = 1
        r_direction = True
        for _ in range(time):
            if r_direction:
                now_person += 1
            else:
                now_person -= 1
            r_direction = self.change_direction(r_direction, now_person, n)
        return now_person

    def change_direction(self, r_direction: bool, now_person: int, n: int):
        return not r_direction if now_person in [1, n] else r_direction
