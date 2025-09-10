# Import library
import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

# inisiate
app = FastAPI() #Fungsi FastAPI

#Choose Dir
BASE_DIR = Path(__file__).resolve().parent.parent
HTML_DIR = BASE_DIR / "html"

# Main Endpoint
@app.get("/", response_class=HTMLResponse)
async def ListHTML():   # Fungsi untuk show List HTML file ( daripada dibuka 1/1 ga efektif )
    try:
        files = sorted([f for f in os.listdir(HTML_DIR) if f.endswith('.html')])
        links = "".join([f'<li><a href="/{file}">{file}</a></li>' for file in files])
        content = f"""
        <!DOCTYPE html>
        <html lang="id">
        <head>
            <title>File Server</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {{ font-family: system-ui, sans-serif; padding: 2rem; background-color: #f8f9fa; }}
                .container {{ max-width: 700px; margin: auto; padding: 2rem; background-color: white; border-radius: 0.5rem; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
                ul {{ list-style-type: none; padding: 0; }}
                a {{ display: block; padding: 0.75rem 1rem; margin-bottom: 0.5rem; background-color: #e9ecef; color: #212529; text-decoration: none; border-radius: 0.25rem; transition: background-color 0.2s; }}
                a:hover {{ background-color: #dee2e6; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Endpoint Test File</h1>
                <ul>{links}</ul>
            </div>
        </body>
        </html>
        """
        return HTMLResponse(content=content)
    except FileNotFoundError:
        return HTMLResponse(content="<h1>Error: Direktori 'html' tidak ditemukan.</h1>", status_code=500)

# Endpoint Check
@app.get("/api/check") #Fungsi Checking 
def check():
    return {"status": "ok", "message": "API is running!"}

# Static File Mounting
app.mount("/", StaticFiles(directory=HTML_DIR), name="html")    # Fungsi Mount