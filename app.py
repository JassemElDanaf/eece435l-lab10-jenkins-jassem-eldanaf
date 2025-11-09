def greet(name):
    """Simple greet function for demonstration."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    # Produce a tiny artifact to demonstrate a deploy/archive step
    from datetime import datetime, UTC
    import os

    os.makedirs("dist", exist_ok=True)
    with open(os.path.join("dist", "artifact.txt"), "w", encoding="utf-8") as f:
        f.write(f"Build artifact generated at {datetime.now(UTC).isoformat()}Z\n")
    print("Wrote dist/artifact.txt")
