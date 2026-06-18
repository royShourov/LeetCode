class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutes_angle = minutes * 6
        hours_angle = 30 * hour + 0.5 * minutes

        angle = abs(hours_angle - minutes_angle)
        return min(angle, 360 - angle)