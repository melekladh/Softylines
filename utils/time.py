
def extract_segments(result):
    """
    Takes the full result from extract() and returns segment-level timestamps.
    Each segment includes: start time, end time, and the spoken text.
    """
    if "chunks" not in result:
        raise ValueError("Timestamps not found in result. Did you set return_timestamps=True in your pipeline?")

    segments = []

    for chunk in result["chunks"]:
        segment = {
            "start": chunk.get("timestamp", [None])[0],
            "end": chunk.get("timestamp", [None])[1],
            "text": chunk.get("text", "").strip()
        }
        segments.append(segment)

    return segments
