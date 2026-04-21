# QR Code Restaurant Menu

Generate a QR code that links to your restaurant menu image and Instagram page.

## Setup

1. **Install dependencies:**
   ```bash
   pip install qrcode[pil]
   ```

2. **Start the server:**
   ```bash
   python server.py
   ```

3. **Print the QR code:**
   - The `qr-code.png` file will be generated
   - Print and display it at your restaurant

## How It Works

1. Customer scans QR code with phone
2. Opens landing page showing:
   - Your restaurant menu (menu.jpg)
   - Instagram link to your profile
3. They can click the Instagram button or just view the menu

## Files

- `server.py` - Web server (run this)
- `menu.html` - Landing page customers see
- `qr-code.png` - Generated QR code (displays menu from Google Drive)

## Customize

Edit `menu.html` to:
- Change restaurant name
- Change Instagram URL
- Modify colors and styling
