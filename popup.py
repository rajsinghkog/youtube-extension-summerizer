from fastapi import FastAPI, HTTPException
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi


app = FastAPI()


summarizer = pipeline('summarization', model='sshleifer/distilbart-cnn-12-6', device=-1)

@app.get("/summary")
async def summary_api(url: str):
    try:
        # Extract the video ID from the URL
        video_id = url.split('v=')[1].split('&')[0]
        transcript = get_transcript(video_id)
        summary = summarizer(transcript)
        return {"summary": summary[0]['summary_text']}
    except Exception as e:
       
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

def get_transcript(video_id: str) -> str:
    try:
       
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ' '.join([entry['text'] for entry in transcript_list])
        return transcript
    except Exception as e:
        # Handle error in transcript fetching
        raise HTTPException(status_code=400, detail=f"Error fetching transcript: {str(e)}")

