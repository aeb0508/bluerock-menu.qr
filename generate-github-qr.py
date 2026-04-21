import qrcode

# Netlify deployment URL
netlify_url = "https://bluerock-menu.netlify.app/"

img = qrcode.make(netlify_url)
img.save("qr-code.png")

print(f"✓ QR code generated: qr-code.png")
print(f"✓ Points to: {netlify_url}")
print(f"\nDeployed on Netlify")
print(f"Site: https://bluerock-menu.netlify.app/")
