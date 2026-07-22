#!/usr/bin/env python3
"""Local dev server for the EdMo Grows site.

Same as `python3 -m http.server` but sends no-cache headers so browsers
always fetch the latest files — no more stale pages or sideways images.
"""
import http.server

PORT = 4173


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, must-revalidate")
        super().end_headers()


if __name__ == "__main__":
    http.server.ThreadingHTTPServer(("", PORT), NoCacheHandler).serve_forever()
