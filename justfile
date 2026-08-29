build:
    python3 scripts/build_posts.py

serve: build
    python3 -m http.server 8000
