#!/usr/bin/env python3

import asyncio
import edge_tts
from playsound import playsound

VOICE = "zh-CN-YunxiNeural" # Chinese
OUTPUT_FILE = "temp.mp3"

async def speak(text: str) -> None:
    """Convert text to speech and save to a file."""
    communicate = edge_tts.Communicate(text, VOICE)
    with open(OUTPUT_FILE, "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                print(f"WordBoundary: {chunk}")
    # Play the saved audio file
    playsound(OUTPUT_FILE)

async def amain() -> None:
    """Main function to keep running and take user input."""
    while True:
        text = input("Enter text to speak ('quit' to exit): ")
        if text.lower() == 'quit':
            print("Exiting program.")
            break
        await speak(text)

if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    try:
        loop.run_until_complete(amain())
    finally:
        loop.close()
