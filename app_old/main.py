def add(a: int, b: int) -> int:
    """Simple add function for demonstration."""
    return a + b


if __name__ == "__main__":
    # Produce a tiny artifact to demonstrate a deploy/archive step
    from datetime import datetime
    import os

    os.makedirs("dist", exist_ok=True)
    with open(os.path.join("dist", "artifact.txt"), "w", encoding="utf-8") as f:
        f.write(f"Build artifact generated at {datetime.utcnow().isoformat()}Z\n")
    print("Wrote dist/artifact.txt")
