import json
import os
from datetime import datetime

class StatsManager:
    def __init__(self, stats_file="stats.json"):
        self.stats_file = stats_file
        self.history = []
        self.load()

    def load(self):
        if os.path.exists(self.stats_file):
            try:
                with open(self.stats_file, 'r', encoding='utf-8') as f:
                    self.history = json.load(f)
            except Exception as e:
                pass # Silent fail or log

    def log_session(self, summary):
        session_data = summary.copy()
        session_data["timestamp"] = datetime.now().isoformat()
        self.history.append(session_data)
        self.save()

    def save(self):
        try:
            with open(self.stats_file, 'w', encoding='utf-8') as f:
                json.dump(self.history, f, indent=4, ensure_ascii=False)
        except Exception as e:
            pass

    def get_best_runs(self, limit=10):
        # Sort by score descending
        return sorted(self.history, key=lambda x: x.get("score", 0), reverse=True)[:limit]
