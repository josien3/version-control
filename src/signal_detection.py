
import scipy.stats as stats
import numpy as np

class SignalDetection:
    def __init__(self, hits, misses, false_alarms, correct_rejections):
        self.hits = hits
        self.misses = misses
        self.false_alarms = false_alarms
        self.correct_rejections = correct_rejections

    def hit_rate(self):
        """Calculates the hit rate."""
        return self.hits / (self.hits + self.misses) if (self.hits + self.misses) > 0 else 0

    def false_alarm_rate(self):
        """Calculates the false alarm rate."""
        return self.false_alarms / (self.false_alarms + self.correct_rejections) if (self.false_alarms + self.correct_rejections) > 0 else 0

    def d_prime(self):
        """Calculates d' (d-prime) to measure sensitivity."""
        H = self.hit_rate()
        FA = self.false_alarm_rate()

        # Preventing extreme values (0 or 1) that break z-score calculation
        H = min(max(H, 1e-6), 1 - 1e-6)
        FA = min(max(FA, 1e-6), 1 - 1e-6)

        return stats.norm.ppf(H) - stats.norm.ppf(FA)

    def criterion(self):
        """Calculates the criterion (C) for response bias."""
        H = self.hit_rate()
        FA = self.false_alarm_rate()

        # Preventing extreme values (0 or 1)
        H = min(max(H, 1e-6), 1 - 1e-6)
        FA = min(max(FA, 1e-6), 1 - 1e-6)

        return -0.5 * (stats.norm.ppf(H) + stats.norm.ppf(FA))

    def summary(self):
        """Returns a summary of all calculations."""
        return {
            "Hit Rate": self.hit_rate(),
            "False Alarm Rate": self.false_alarm_rate(),
            "D-Prime": self.d_prime(),
            "Criterion": self.criterion(),
        }

# Ensure script runs when executed
if __name__ == "__main__":
    # Example data
    sd = SignalDetection(hits=40, misses=10, false_alarms=15, correct_rejections=35)
    
    # Print results
    print("Signal Detection Summary:")
    for key, value in sd.summary().items():
        print(f"{key}: {value:.4f}")  # Print results with 4 decimal places




