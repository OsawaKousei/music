import os
from glob import glob

import music21

from transformer_utils import parse_midi_files

MIDI_FILES_DIR = "data"


def main() -> None:
    parser = music21.converter
    seq_len = 32
    parsed_data_path = "parsed_data"

    if not os.path.exists(parsed_data_path):
        os.makedirs(parsed_data_path)

    file_list = glob(os.path.join(MIDI_FILES_DIR, "*.mid"))
    notes_list, duration_list = parse_midi_files(
        file_list, parser, seq_len, parsed_data_path
    )

    print(f"Parsed {len(notes_list)} sequences of notes and durations.")


if __name__ == "__main__":
    main()
