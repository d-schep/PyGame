import os

# Arquivo onde guardamos os recordes
HIGH_SCORES_FILE = "high_scores.txt"
DEFAULT_TIME = 900  # 15 minutos em segundos

def load_high_scores():
    """Carrega os recordes do arquivo de texto."""
    try:
        # Se o arquivo existe, lê os recordes
        if os.path.exists(HIGH_SCORES_FILE):
            with open(HIGH_SCORES_FILE, 'r') as f:
                # Lê cada linha e converte para número
                scores = [int(line.strip()) for line in f.readlines()]
                # Se tiver menos de 3 recordes, completa com o tempo padrão
                while len(scores) < 3:
                    scores.append(DEFAULT_TIME)
                return scores[:3]  # Retorna só os 3 melhores
    except Exception as e:
        print(f"Erro ao carregar recordes: {e}")
    
    # Se algo der errado, retorna 3 recordes padrão
    return [DEFAULT_TIME, DEFAULT_TIME, DEFAULT_TIME]

def save_high_scores(scores):
    """Salva os recordes no arquivo de texto."""
    try:
        with open(HIGH_SCORES_FILE, 'w') as f:
            for score in scores:
                f.write(f"{score}\n")
    except Exception as e:
        print(f"Erro ao salvar recordes: {e}")

def update_high_scores(new_time):
    """Atualiza os recordes com um novo tempo, se for melhor que os existentes."""
    try:
        # Carrega os recordes atuais
        scores = load_high_scores()
        # Adiciona o novo tempo
        scores.append(new_time)
        # Ordena do menor para o maior (menor tempo = melhor)
        scores.sort()
        # Pega só os 3 melhores
        scores = scores[:3]
        # Salva os novos recordes
        save_high_scores(scores)
        return scores
    except Exception as e:
        print(f"Erro ao atualizar recordes: {e}")
        return [DEFAULT_TIME, DEFAULT_TIME, DEFAULT_TIME]

def format_time(seconds):
    """Formata o tempo em segundos para o formato MM:SS."""
    try:
        minutes = int(seconds) // 60
        seconds = int(seconds) % 60
        return f"{minutes:02d}:{seconds:02d}"
    except Exception as e:
        print(f"Erro ao formatar tempo: {e}")
        return "15:00"  # Retorna tempo padrão se algo der errado 