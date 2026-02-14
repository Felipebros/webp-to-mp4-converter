import os
import numpy as np
from PIL import Image, ImageSequence
from moviepy import ImageSequenceClip


def convert_webp_to_mp4(input_path, output_path):
    print(f"Lendo arquivo: {input_path}")
    try:
        with Image.open(input_path) as img:
            frames = []
            durations = []

            width, height = img.size
            new_width = width if width % 2 == 0 else width - 1
            new_height = height if height % 2 == 0 else height - 1

            print(f"Dimensões originais: {width}x{height}")

            for frame in ImageSequence.Iterator(img):
                # Capturar a duração do frame (em ms)
                d = frame.info.get(
                    "duration", 40
                )  # Padrão 40ms (25fps) se não encontrar
                durations.append(d)

                frame_rgb = frame.convert("RGB")
                if new_width != width or new_height != height:
                    frame_rgb = frame_rgb.resize(
                        (new_width, new_height), Image.Resampling.LANCZOS
                    )
                frames.append(np.array(frame_rgb))

            # Calcular FPS baseado na média das durações
            avg_duration = sum(durations) / len(durations) if durations else 40
            detected_fps = 1000.0 / avg_duration

            print(f"Total de frames: {len(frames)}")
            print(
                f"Duração média detectada: {avg_duration:.2f}ms (FPS: {detected_fps:.2f})"
            )

            if not frames:
                print("Nenhum frame encontrado.")
                return

            # Criar o clipe de vídeo com o FPS detectado
            clip = ImageSequenceClip(frames, fps=detected_fps)

            print(f"Salvando em: {output_path}")
            clip.write_videofile(
                output_path,
                codec="libx264",
                audio=False,
                preset="medium",
                ffmpeg_params=[
                    "-pix_fmt",
                    "yuv420p",
                    "-profile:v",
                    "high",
                    "-level",
                    "4.0",
                ],
            )
            print("Conversão concluída com sucesso!")

    except Exception as e:
        print(f"Erro durante a conversão: {e}")


if __name__ == "__main__":
    # Caminhos baseados no seu ambiente
    input_file = r"input.webp"
    output_file = r"output.mp4"

    if os.path.exists(input_file):
        convert_webp_to_mp4(input_file, output_file)
    else:
        print(f"Arquivo de entrada não encontrado: {input_file}")
