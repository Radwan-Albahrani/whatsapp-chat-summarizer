# Whatsapp chat summarizer

This is a simple python script that reads a whatsapp chat file and summarizes it. It uses Gemini to summarize the chat, while anonymizing the names of the participants.

## Usage

1. Export the chat from whatsapp
2. Run the script in `main.py`
3. Enter the path to the chat file
4. The script will generate a summary of the chat

## Dependencies

Run the following command to install the requirements:

```bash
pip install -r requirements.txt
```

## ENV FILE

Create a `.env` file in the root directory with the following content:

```env
GEMINI_API_KEY=YOUR_API_KEY
```
