class LeaderboardManager:
    def __init__(self, stats_manager):
        self.stats_manager = stats_manager
        self.sort_by = "score"  # "score" or "time"

    def toggle_sort(self):
        self.sort_by = "time" if self.sort_by == "score" else "score"

    def get_top_scores(self, limit=10):
        return self.stats_manager.get_best_runs(limit, sort_by=self.sort_by)

    def format_leaderboard(self):
        top_scores = self.get_top_scores()
        sort_label = "BY SCORE" if self.sort_by == "score" else "BY SURVIVAL TIME"
        lines = []
        lines.append(f"Sorted: {sort_label}  (Press 'S' to toggle)")
        lines.append("")
        lines.append(f"{'Rank':<5} {'Player':<15} {'Score':<10} {'Length':<8} {'Time':<8}")
        lines.append("-" * 50)
        for i, run in enumerate(top_scores, 1):
            player = run.get("player", "Unknown")
            score = run.get("score", 0)
            length = run.get("snake_length", 0)
            duration = run.get("time_survived", 0)
            lines.append(f"{i:<5} {player:<15} {score:<10} {length:<8} {duration:<8}s")
        return "\n".join(lines)
