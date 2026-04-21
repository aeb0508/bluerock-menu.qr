import qrcode

# GitHub Pages URL with bluerock-menu.qr repository
github_url = "https://aeb0508.github.io/bluerock-menu.qr/"

img = qrcode.make(github_url)
img.save("qr-code.png")

print(f"✓ QR code generated: qr-code.png")
print(f"✓ Points to: {github_url}")
print(f"\nRepository name: bluerock-menu.qr")
print(f"GitHub username: aeb0508")
