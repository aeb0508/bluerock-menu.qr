import http.server
import socketserver
import os
import qrcode
import webbrowser

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Generate QR code pointing to localhost
qr_url = f'http://localhost:{PORT}/menu.html'
img = qrcode.make(qr_url)
img.save('qr-code.png')
print(f"✓ QR code generated: qr-code.png")

print(f"\n✓ Starting server on http://localhost:{PORT}")
print(f"✓ Menu accessible at: http://localhost:{PORT}/menu.html")
print(f"✓ Press Ctrl+C to stop the server\n")

try:
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"✓ Server running...")
        print(f"✓ Scan the QR code with your phone to test it\n")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n✓ Server stopped")
