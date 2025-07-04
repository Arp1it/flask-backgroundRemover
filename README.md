# Background Remover Flask App

A simple Flask application that removes the background from uploaded images using the `rembg` library.

## Requirements

- Python 3.x
- Flask
- rembg
- werkzeug

Install required packages:

```bash
pip install flask rembg werkzeug
````

## Project Structure

```Structure
├── main.py
├── static/
│   ├── upload/
│   └── opl/
|   └── upload/
├── templates/
│   ├── index.html
│   └── main.html
└── README.md
```

## How to Run

1. Create required directories:

```bash
mkdir -p static/upload static/opl templates
```

2. Add `index.html` and `main.html` to the `templates/` directory.

3. Run the Flask application:

```bash
python main.py
```

4. Open the app in your browser:

```bash
http://127.0.0.1:5000
```

## Usage

* Upload an image using the form on the page.
* The image will be saved in `static/upload/`.
* The background will be removed using `rembg`.
* The processed image will be saved in `static/opl/` and displayed on the same page with a download option.
