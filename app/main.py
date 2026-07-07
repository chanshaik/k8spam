from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>k8spam App</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #282c34;
                color: #ffffff;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background-color: #20232a;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 8px 16px rgba(0,0,0,0.5);
                text-align: center;
            }
            h1 {
                color: #61dafb;
                margin-bottom: 10px;
            }
            p {
                font-size: 1.2rem;
                color: #a9a9a9;
            }
            .btn {
                background-color: #61dafb;
                color: #282c34;
                border: none;
                padding: 15px 30px;
                font-size: 1rem;
                font-weight: bold;
                border-radius: 8px;
                cursor: pointer;
                margin-top: 20px;
                transition: transform 0.2s, background-color 0.2s;
            }
            .btn:hover {
                background-color: #21a1c4;
                transform: scale(1.05);
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 k8spam is Live!</h1>
            <p>Running inside a Kubernetes Pod on Minikube.</p>
            <button class="btn" onclick="changeColor()">Click for Magic</button>
        </div>

        <script>
            function changeColor() {
                const colors = ['#61dafb', '#ff6b6b', '#4ecdc4', '#ffe66d', '#ff9f43'];
                const randomColor = colors[Math.floor(Math.random() * colors.length)];
                document.querySelector('h1').style.color = randomColor;
                document.querySelector('.btn').style.backgroundColor = randomColor;
            }
        </script>
    </body>
    </html>
    """
    return html_content

@app.get("/health")
def health_check():
    return {"status": "healthy"}
