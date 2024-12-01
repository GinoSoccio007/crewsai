from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
import os
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HTML_CONTENT = """
<!DOCTYPE html>
<html>
<head>
    <title>CrewAI Interface</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            max-width: 800px; 
            margin: 0 auto; 
            padding: 20px;
        }
        .container { 
            background-color: #f9f9f9; 
            padding: 20px; 
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        textarea, input { 
            width: 100%; 
            padding: 10px; 
            margin: 10px 0; 
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        #result {
            white-space: pre-wrap;
            margin-top: 20px;
            padding: 15px;
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>CrewAI Research Interface</h1>
        <form id="researchForm" onsubmit="submitForm(event)">
            <div>
                <label for="topic">Research Topic:</label>
                <textarea id="topic" name="topic" rows="3" required></textarea>
            </div>
            <div>
                <label for="api_key">OpenAI API Key:</label>
                <input type="password" id="api_key" name="api_key" required>
            </div>
            <button type="submit">Generate Research</button>
        </form>
        <div id="result"></div>
    </div>

    <script>
        async function submitForm(event) {
            event.preventDefault();
            const resultDiv = document.getElementById('result');
            res
