This script is idented to play live broadcast content from mitele.es

Require requests

# Usage

_Choose channel and play (check the player path in the source)_

./get.py

_Get link channel (must be used within the script session, see example below)_

./get.py <telecinco|cuatro|boing|divinity|fdf|energy|bemad|futbol-mitele>

__Examples__

Linux: mpv \`./get.py boing\`

Windows (Powershell): & 'C:\Program Files\VideoLAN\VLC\vlc.exe' (python .\get.py boing)

Note: telecinco and cuatro may not work
