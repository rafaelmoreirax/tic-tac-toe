def print_board(board):
    """Exibe o tabuleiro do jogo da velha."""
    print("\n")
    for i in range(1, 8, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 7:
            print("---+---+---")
    print("\n")

def check_winner(board, player):
    """Verifica se o jogador venceu."""
    # Linhas
    for i in range(1, 8, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Colunas
    for i in range(1, 4):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Diagonais
    if board[1] == board[5] == board[9] == player:
        return True
    if board[3] == board[5] == board[7] == player:
        return True
    return False

def is_board_full(board):
    """Verifica se o tabuleiro está cheio."""
    return all(board[i] != str(i) for i in range(1, 10))

def is_valid_move(board, move):
    """Verifica se a jogada é válida."""
    try:
        move = int(move)
        if 1 <= move <= 9 and board[move] == str(move):
            return True
        return False
    except ValueError:
        return False

def make_move(board, move, player):
    """Realiza a jogada no tabuleiro."""
    board[move] = player

def play_game():
    """Executa o jogo da velha."""
    board = ['0'] + [str(i) for i in range(1, 10)]  # Tabuleiro: índices 1-9
    current_player = 'X'

    print("Bem-vindo ao Jogo da Velha!")
    print("Use números de 1 a 9 para jogar.")
    print_board(board)

    while True:
        # Solicita jogada
        move = input(f"Jogador {current_player}, escolha uma posição (1-9): ")
        
        # Valida jogada
        if not is_valid_move(board, move):
            print("Jogada inválida! Tente novamente.")
            continue
        
        # Realiza jogada
        move = int(move)
        make_move(board, move, current_player)
        print_board(board)

        # Verifica vitória
        if check_winner(board, current_player):
            print(f"Jogador {current_player} venceu!")
            break

        # Verifica empate
        if is_board_full(board):
            print("Empate!")
            break

        # Alterna jogador
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()