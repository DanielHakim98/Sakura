from dataclasses import dataclass
import requests

ANKI_CONNECT_URL = "http://localhost:8765"
DECK_NAME = "Jlab's beginner course::Part 1: Listening comprehension"


def invoke(action, **params) -> dict:
    body = {"action": action, "version": 6, "params": params}
    print(body)
    return requests.post(ANKI_CONNECT_URL, json=body).json()


def get_note_ids(deck_name):
    query_builder = ""
    for param in [f'deck:"{deck_name}"', "is:new", "note:JlabNote-JlabConverted-1"]:
        query_builder += param + " "
    return invoke("findNotes", query=query_builder)


def get_notes_info(note_id):
    return invoke("notesInfo", notes=[note_id])


def update_note(note_id, fields):
    return invoke("updateNote", note={"id": note_id, "fields": fields})


@dataclass
class Wanted:
    other_front: str
    jlab_kanji: str
    jlab_clozefront: str
    jlab_clozeback: str
    jlab_listeningfront: str


def main():
    res = get_note_ids(DECK_NAME)
    ids = res.get("result", [])

    wanted = Wanted(
        other_front="Other-Front",
        jlab_kanji="Jlab-Kanji",
        jlab_clozefront="Jlab-ClozeFront",
        jlab_clozeback="Jlab-ClozeBack",
        jlab_listeningfront="Jlab-ListeningFront",
    )

    for id in ids:
        note_info = get_notes_info(id).get("result", [])

        if len(note_info) == 0:
            print(f"note info '{id}' unavailable")

        note_info_fields = note_info[0]["fields"]
        updated_fields = {
            wanted.jlab_clozefront: note_info_fields[wanted.jlab_kanji]["value"],
            wanted.jlab_clozeback: note_info_fields[wanted.other_front]["value"],
            wanted.jlab_listeningfront: "",
        }
        res = update_note(id, updated_fields)
        print(res)


if __name__ == "__main__":
    main()
