import os

def CreateHTML(filepath, KBsize):
    TargetSize = KBsize * 1024
    FillerLine = "<!--" + (" " * 1016) + "-->\n"
    
    assert len(FillerLine.encode('utf-8')) == 1024
    NumLines = TargetSize // len(FillerLine.encode('utf-8'))
    
    try:
        with open(filepath, 'w') as f:
            f.write("</head>\n<body>\n")
            f.write(f"  <h1>Test File API {KBsize}KB</h1>\n")
            
            for _ in range(NumLines):
                f.write(FillerLine)
                
            f.write("</body>\n</html>\n")
        
        with open(filepath, 'rb+') as f:
            f.truncate(TargetSize)

        print(f"done : {filepath} ({os.path.getsize(filepath) / 1024:.2f} KB)")

    except IOError as e:
        print(f"Error pak {filepath}: {e}")

if __name__ == "__main__":
    HTML_DIR = "html"
    if not os.path.exists(HTML_DIR):
        os.makedirs(HTML_DIR)

    KBHTML = {
        "10kb.html": 10,
        "100kb.html": 100,
        "1mb.html": 1 * 1024,
        "5mb.html": 5 * 1024,
        "10mb.html": 10 * 1024
    }
    
    for filename, size in KBHTML.items():
        filepath = os.path.join(HTML_DIR, filename)
        CreateHTML(filepath, size)