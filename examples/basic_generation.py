#!/usr/bin/env python3

import asyncio
import edge_tts
from playsound import playsound

VOICE = "en-GB-SoniaNeural"
OUTPUT_FILE = "temp.mp3"

async def speak(text: str) -> None:
    """Function to convert text to speech and play it."""
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(OUTPUT_FILE)
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
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(amain())
    finally:
        loop.close()
