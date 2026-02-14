# WebP to MP4 Converter

Um conversor simples e eficiente escrito em Python para transformar arquivos WebP animados em vídeos MP4 de alta compatibilidade.

## ✨ Diferenciais
- **Ajuste de Dimensões:** Garante que o vídeo tenha dimensões pares (necessário para o codec H.264).
- **Detecção de FPS:** Lê automaticamente a duração dos frames do WebP original para manter a sincronia perfeita.
- **Alta Compatibilidade:** Utiliza o formato de pixel `yuv420p` e o perfil `high` para funcionar em qualquer player do Windows ou MacOS.

## 🚀 Como usar

### 1. Requisitos
- Python 3.7+
- FFmpeg instalado no sistema (ou o MoviePy fará o download automático se necessário).

### 2. Instalação
Crie um ambiente virtual e instale as dependências:
```bash
python -m venv .venv
source .venv/Scripts/activate  # No Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Execução
Edite o arquivo `main.py` com os caminhos dos seus arquivos e execute:
```bash
python main.py
```

## 🛠️ Tecnologias
- [Pillow](https://python-pillow.org/) - Processamento de frames.
- [MoviePy](https://zulko.github.io/moviepy/) - Edição e codificação de vídeo.
- [NumPy](https://numpy.org/) - Manipulação de arrays de imagem.
