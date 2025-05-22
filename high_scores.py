import json
import os

HIGH_SCORES_FILE = "high_scores.json"

def load_high_scores():
    """Load the high scores from the JSON file."""
    try:
        if os.path.exists(HIGH_SCORES_FILE):
            with open(HIGH_SCORES_FILE, 'r') as f:
                scores = json.load(f)
                # Garante que temos exatamente 3 scores
                while len(scores) < 3:
                    scores.append(900)  # 15 minutos em segundos
                return scores[:3]  # Retorna apenas os 3 primeiros
    except:
        pass
    # Se algo der errado, retorna 3 scores padrão
    return [900, 900, 900]  # 15 minutos em segundos

def save_high_scores(scores):
    """Save the high scores to the JSON file."""
    try:
        with open(HIGH_SCORES_FILE, 'w') as f:
            json.dump(scores, f)
    except:
        pass  # Se não conseguir salvar, continua sem salvar

def update_high_scores(new_time):
    """Update the high scores with a new time if it's better than existing ones."""
    try:
        scores = load_high_scores()
        scores.append(new_time)
        scores.sort()  # Sort in ascending order
        scores = scores[:3]  # Keep only top 3
        save_high_scores(scores)
        return scores
    except:
        return [900, 900, 900]  # Retorna valores padrão se algo der errado

def format_time(seconds):
    """Format time in seconds to MM:SS format."""
    try:
        minutes = int(seconds) // 60
        seconds = int(seconds) % 60
        return f"{minutes:02d}:{seconds:02d}"
    except:
        return "15:00"  # Retorna tempo padrão se algo der errado 